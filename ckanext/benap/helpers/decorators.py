def decorator_timer(func):
    import time
    import logging
    import functools
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):      
        tic = time.time()
        value = func(*args, **kwargs)
        toc = time.time()
        elapsed_time =toc - tic
        logging.error('TimeWillTell5 %s in round time: %s seconds', func.__name__, elapsed_time)
        return value
    return wrapper_timer