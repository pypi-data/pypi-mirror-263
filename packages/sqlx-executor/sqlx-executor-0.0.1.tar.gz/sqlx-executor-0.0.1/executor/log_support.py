from logging import basicConfig, INFO, getLogger

logger = getLogger(__name__)
basicConfig(level=INFO, format='[%(levelname)s]: %(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def db_ctx_log(action, connection):
    logger.debug("%s connection <%s>..." % (action, hex(id(connection))))

