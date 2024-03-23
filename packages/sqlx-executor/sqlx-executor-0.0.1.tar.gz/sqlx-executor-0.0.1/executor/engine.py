from enum import Enum


class EngineName(Enum):
    MYSQL = 'MySQL'
    POSTGRESQL = 'PostgreSQL'
    ORACLE = 'Oracle'
    SQL_SERVER = 'SQL Server'
    SQLITE = 'SQLite'
    UNKNOW = 'Unknow'


class Driver(Enum):
    MYSQL_CLIENT = 'MySQLdb'
    PYMYSQL = 'pymysql'
    MYSQL_CONNECTOR = 'mysql.connector'
    PSYCOPG2 = 'psycopg2'
    PG8000 = 'pg8000'
    PY_POSTGRESQL = 'postgresql.driver.dbapi20'
    PYGRESQL = 'pgdb'
    ORACLEDB = 'oracledb'
    SQLITE3 = 'sqlite3'


DRIVER_ENGINE_DICT = {
    Driver.MYSQL_CLIENT.value: EngineName.MYSQL,
    Driver.PYMYSQL.value: EngineName.MYSQL,
    Driver.MYSQL_CONNECTOR.value: EngineName.MYSQL,
    Driver.PSYCOPG2.value: EngineName.POSTGRESQL,
    Driver.PG8000.value: EngineName.POSTGRESQL,
    Driver.PY_POSTGRESQL.value: EngineName.POSTGRESQL,
    Driver.PYGRESQL.value: EngineName.POSTGRESQL,
    Driver.ORACLEDB.value: EngineName.ORACLE,
    Driver.SQLITE3.value: EngineName.SQLITE
}