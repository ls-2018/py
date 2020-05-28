import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, stop_after_delay, wait_exponential, wait_fixed, \
    wait_random, retry_if_result, retry_if_exception_type

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 5  # 设定尝试次数
max_times = 5  # 设定重试间隔
wait_seconds = 2  # 重试前等待固定时间


def is_none_p(value):
    pass


@retry(
    stop=stop_after_delay(max_times) | stop_after_attempt(max_tries),  # 设定重试间隔
    wait=wait_fixed(wait_seconds),  # 设定重试时间
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
    retry=(retry_if_result(is_none_p) | retry_if_exception_type(Exception))  # 带有触发条件的retry语句
)
def init():
    try:
        # Try to create session to check if DB is awake
        raise IOError('2')
        # 自定义在哪些Exception进行重试
        # 自定义在哪些返回值的情况进行重试
        # 协程的重试
    except IOError as e:
        logger.error(e)
        raise e


def main():
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()

'''
wait = wait_fixed(wait_seconds)
wait = wait_random(min=1, max=2)
# 重试时间间隔满足：2^n * multiplier, n为重试次数，但最多间隔10秒,最多重试三次
wait = wait_exponential(multiplier=2, min=3, max=100)   #按照指数的等待时间

'''
