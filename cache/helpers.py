import time
from functools import wraps
import re

# Decorator to measure execution time
def measure_time(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.time()
        result = func(self, *args, **kwargs)
        end = time.time()
        elapsed_time = end - start
        self.time_logger.info(
            f"Execution time of {func.__name__}: {elapsed_time} seconds"
        )
        return result
    return wrapper

def re_eval(value):
    pattern = r'^[a-zA-Z0-9]+$'
    print(value)
    return re.match(pattern, value["value"])        
