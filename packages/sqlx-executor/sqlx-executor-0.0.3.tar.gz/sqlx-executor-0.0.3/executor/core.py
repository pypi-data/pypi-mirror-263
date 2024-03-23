# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import functools
from .log_support import logger
from .init_import import import_driver, get_engine
from .support import DBCtx, ConnectionCtx, TransactionCtx, try_commit, DBError, DB_LOCK
from .constant import PARAM_DRIVER, PARAM_DEBUG, PARAM_POOL_SIZE
from .engine import EngineName, Driver

_DB_CTX = None
_POOLED = False


def init_db(*args, **kwargs) -> EngineName:
    """
    Compliant with the Python DB API 2.0 (PEP-249).

    from executor
    executor.init_db('test.db', driver='sqlite3', debug=True)
    or
    executor.init_db("postgres://user:password@127.0.0.1:5432/testdb", driver='psycopg2', pool_size=5, debug=True)
    or
    executor.init_db(user='root', password='xxx', host='127.0.0.1', port=3306, database='testdb', driver='pymysql', pool_size=5, debug=True)

    Addition parameters:
    :param driver=None: str, import driver, 'import pymysql'
    :param pool_size=0: int, default 0, size of connection pool
    :param debug=False: bool, if True, print debug context

    Other parameters of connection pool refer to DBUtils: https://webwareforpython.github.io/DBUtils/main.html#pooleddb-pooled-db
    """

    global _DB_CTX
    pool_size = 0
    driver_name = kwargs.pop(PARAM_DRIVER) if PARAM_DRIVER in kwargs else None

    curr_engine_name = get_engine(driver_name, *args, **kwargs)
    engine_name, driver_name, creator = import_driver(driver_name, curr_engine_name)
    prepared = Driver.MYSQL_CONNECTOR.value == driver_name
    if PARAM_DEBUG in kwargs and kwargs.pop(PARAM_DEBUG):
        from logging import DEBUG
        logger.setLevel(DEBUG)

    if PARAM_POOL_SIZE in kwargs:
        # mysql.connector 用自带连接池
        pool_size = kwargs[PARAM_POOL_SIZE] if prepared else kwargs.pop(PARAM_POOL_SIZE)

    pool_args = ['mincached', 'maxcached', 'maxshared', 'maxconnections', 'blocking', 'maxusage', 'setsession', 'reset', 'failures', 'ping']
    pool_kwargs = {key: kwargs.pop(key) for key in pool_args if key in kwargs}
    connect = lambda: creator.connect(*args, **kwargs)
    if pool_size >= 1 and not prepared:
        from .pooling import pooled_connect
        global _POOLED
        _POOLED = True
        connect = pooled_connect(connect, pool_size, **pool_kwargs)

    with DB_LOCK:
        if _DB_CTX is not None:
            raise DBError('DB is already initialized.')
        _DB_CTX = DBCtx(connect=connect, prepared=prepared)

    if pool_size > 0:
        logger.info("Inited db engine <%s> of %s with driver: '%s' and pool size: %d." % (hex(id(_DB_CTX)), engine_name.value,
                                                                                          driver_name, pool_size))
    else:
        logger.info("Inited db engine <%s> of %s with driver: '%s'." % (hex(id(_DB_CTX)), engine_name.value, driver_name))

    return engine_name


def connection():
    """
    Return ConnectionCtx object that can be used by 'with' statement:

    with connection():
        pass
    """
    global _DB_CTX
    return ConnectionCtx(_DB_CTX)


def with_connection(func):
    """
    Decorator for reuse connection.

    @with_connection
    def foo(*args, **kw):
        f1()
        f2()
    """
    global _DB_CTX

    @functools.wraps(func)
    def _wrapper(*args, **kw):
        with ConnectionCtx(_DB_CTX):
            return func(*args, **kw)
    return _wrapper


def transaction():
    """
    Create a transaction object so can use with statement:

    with transaction():
        pass
    with transaction():
         insert(...)
         update(... )
    """
    global _DB_CTX
    return TransactionCtx(_DB_CTX)


def with_transaction(func):
    """
    A decorator that makes function around transaction.

    @with_transaction
    def update_profile(id, name, rollback):
         u = dict(id=id, name=name, email='%s@test.org' % name, passwd=name, last_modified=time.time())
         insert('person', **u)
         r = update('update person set passwd=%s where id=%s', name.upper(), id)
    """
    global _DB_CTX

    @functools.wraps(func)
    def _wrapper(*args, **kw):
        with TransactionCtx(_DB_CTX):
            return func(*args, **kw)
    return _wrapper


def get_connection():
    global _DB_CTX
    _DB_CTX.try_init()
    return _DB_CTX.connection


def close():
    global _DB_CTX
    global _POOLED

    if _POOLED:
        from .pooling import close_pool
        close_pool()
        _POOLED = False

    if _DB_CTX is not None:
        _DB_CTX.release()
        _DB_CTX = None


@with_connection
def execute(sql: str, *args):
    global _DB_CTX
    cursor = None
    logger.debug("Exec func 'executor.%s', " % 'execute')
    try:
        cursor = _DB_CTX.connection.cursor()
        cursor.execute(sql, args)
        result = cursor.rowcount
        try_commit(_DB_CTX)
        return result
    finally:
        if cursor:
            cursor.close()


@with_connection
def save(select_key: str, sql: str, *args):
    global _DB_CTX
    cursor = None
    logger.debug("Exec func 'executor.%s', 'select_key': %s" % ('save', select_key))
    try:
        cursor = _DB_CTX.connection.cursor()
        cursor.execute(sql, args)
        cursor.execute(select_key)
        result = cursor.fetchone()[0]
        try_commit(_DB_CTX)
        return result
    finally:
        if cursor:
            cursor.close()


def select(sql: str, *args):
    return do_select(sql, *args)[0]


def select_one(sql: str, *args):
    return do_select_one(sql, *args)[0]


@with_connection
def do_select(sql: str, *args):
    global _DB_CTX
    cursor = None
    try:
        cursor = _DB_CTX.cursor()
        cursor.execute(sql, args)
        return cursor.fetchall(), cursor.description
    finally:
        if cursor:
            cursor.close()


@with_connection
def do_select_one(sql: str, *args):
    global _DB_CTX
    cursor = None
    try:
        cursor = _DB_CTX.cursor()
        cursor.execute(sql, args)
        return cursor.fetchone(), cursor.description
    finally:
        if cursor:
            cursor.close()


@with_connection
def batch_execute(sql: str, *args):
    """
    Batch execute sql return effect rowcount
    :param sql: insert into person(name, age) values(%s, %s)  -->  args: [('张三', 20), ('李四', 28)]
    :param args: All number must have same size.
    :return: Effect rowcount
    """
    global _DB_CTX
    cursor = None
    assert args, "*args must not be empty."
    try:
        cursor = _DB_CTX.cursor()
        cursor.executemany(sql, args)
        effect_rowcount = cursor.rowcount
        try_commit(_DB_CTX)
        return effect_rowcount
    finally:
        if cursor:
            cursor.close()
