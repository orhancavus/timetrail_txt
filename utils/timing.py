import time
from functools import wraps


def timing_decorator(func):
    """
    A decorator to measure and log the execution time of any Python function.

    Args:
        func: The function to be timed.

    Returns:
        The wrapped function with timing enabled.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        print(f"Function '{func.__name__}' executed in {duration:.3f} seconds")
        return result

    return wrapper
