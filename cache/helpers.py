import time
from functools import wraps
import re
import psutil
import gc

# Calculate threshold as 70% of total available memory in MB
MEMORY_THRESHOLD_MB = psutil.virtual_memory().total * 0.7 / (1024 * 1024)
# MEMORY_THRESHOLD_MB = 100

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

def measure_memory(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Check memory usage
        result = func(self, *args, **kwargs)
        memory_usage = psutil.virtual_memory().used / (1024 * 1024)  # Convert to MB
        self.memory_logger.info(f"Memory usage of {func.__name__}: {memory_usage} MB")
        # Trigger garbage collection if memory usage exceeds threshold
        if memory_usage > MEMORY_THRESHOLD_MB:
            self.memory_logger.info("Memory usage exceeds threshold. Triggering garbage collection.")
            gc.collect()
        return result
    return wrapper

def re_eval(value):
    pattern = r'^[a-zA-Z0-9]+$'
    print(value)
    return re.match(pattern, value["value"])        
