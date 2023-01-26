def decorator_timer(func):
    import time
    import logging
    import functools
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):      
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time =toc - tic
        logging.error(f"Finished {func.__name__!r} in elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer