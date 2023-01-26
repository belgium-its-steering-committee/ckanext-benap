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
        logging.error('Finished {func.__name__!r} in elapsed time: {elapsed_time:0.4f} seconds')
        return value
    return wrapper_timer