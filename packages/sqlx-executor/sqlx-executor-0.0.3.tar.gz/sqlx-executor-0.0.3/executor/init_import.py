import importlib
from .support import DBError
from .log_support import logger
from .constant import PARAM_PORT, MYSQL_PORT, POSTGRESQL_PORT
from .engine import EngineName, DRIVER_ENGINE_DICT


def import_driver(driver_name, curr_engine_name):
    creator = None
    if driver_name:
        if driver_name not in DRIVER_ENGINE_DICT:
            logger.warning(f"Driver '{driver_name}' not support now, may be you should adapter it youself.")
        engine_name = DRIVER_ENGINE_DICT.get(driver_name, EngineName.UNKNOW)
        creator = do_import(driver_name, engine_name)
        engine_name = engine_name if engine_name else curr_engine_name
    else:
        drivers = dict(filter(lambda x: x[1] == curr_engine_name, DRIVER_ENGINE_DICT.items())) if curr_engine_name and curr_engine_name != EngineName.UNKNOW else DRIVER_ENGINE_DICT
        for driver_name, engine_name in drivers.items():
            try:
                creator = importlib.import_module(driver_name)
                break
            except ModuleNotFoundError:
                pass
        if not creator:
            raise DBError(f"You may forgot install driver, may be one of {list(DRIVER_ENGINE_DICT.keys())} suit you.")
    return engine_name, driver_name, creator


def do_import(driver_name, curr_engine_name):
    try:
        return importlib.import_module(driver_name)
    except ModuleNotFoundError:
        raise DBError(f"Import {curr_engine_name.value} driver '{driver_name}' failed, please sure it was installed or change other driver.")


def get_engine(driver_name: str, *args, **kwargs):
    if driver_name is None:
        if args and 'mysql://' in args[0]:
            return EngineName.MYSQL.value
        elif args and 'postgres://' in args[0]:
            return EngineName.POSTGRESQL
        elif args and '://' not in args[0]:
            return EngineName.SQLITE
        elif PARAM_PORT in kwargs:
            port = kwargs[PARAM_PORT]
            if port == MYSQL_PORT:
                return EngineName.MYSQL
            elif port == POSTGRESQL_PORT:
                return EngineName.POSTGRESQL
    return EngineName.UNKNOW
