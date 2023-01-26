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
        totalTime = round(totalTime + elapsed_time,3)
        logging.error('Finished %s in round time: %s seconds. Total Rounds Time: %s', func.__name__, round(elapsed_time,3), totalTime)
        
        return value
    return wrapper_timer