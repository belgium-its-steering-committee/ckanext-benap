import time
import functools
import logging

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time =toc - tic
        logging.info("TIMER: Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer