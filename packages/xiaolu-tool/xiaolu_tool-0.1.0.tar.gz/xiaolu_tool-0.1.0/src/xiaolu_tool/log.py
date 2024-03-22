import functools
import logging
import time
from logging import handlers
from datetime import datetime
from xiaolu_tool.path import ProjectPath

LOG_PATH = ProjectPath.LOG_PATH


def configure_logging(log_filename="logger"):
    log_filename = (
        f"{LOG_PATH}/{log_filename}_{datetime.now().strftime('%Y%m%d%H%M')}.log"
    )

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s - %(threadName)s - %(module)s] - %(message)s",
        datefmt="%Y%m%d %H:%M:%S",
        handlers=[
            handlers.RotatingFileHandler(log_filename, maxBytes=1e6, backupCount=5),
            logging.StreamHandler(),
        ],
    )


# Call the function to configure logging
configure_logging()


class LogFactory:
    logger = logging.getLogger("logger")

    @classmethod
    def get_logger(cls, logger_name):
        return logging.getLogger(logger_name)


def logit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 打印方法名和参数
        start_time = time.time()

        # 执行原函数
        result = func(*args, **kwargs)

        # 计算执行时间
        execution_time = time.time() - start_time
        # 打印方法名和执行时间
        LogFactory.logger.info(f"Executed {func.__name__!r}: args={args}, kwargs={kwargs}, "
                               f"return={result}, execution time={execution_time:.4f} seconds")
        return result

    return wrapper
