from cache_log.log import MyLogger
import re
import time
from functools import wraps

class Cache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = {}
        self.event_logger = MyLogger('event_logger', 'event_logger.log')
        self.time_logger = MyLogger('time_logger', 'time_logger.log')
        self.event_logger.info("Start event logger")
        self.time_logger.info("Start time logger")

    # Decorator to measure execution time
    def measure_time(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            start_time = time.time()
            result = func(self, *args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.time_logger.info(
                f"Execution time of {func.__name__}: {elapsed_time} seconds"
            )
            return result
        return wrapper

    @measure_time
    def get(self, key):
        if key in self.cache:
            self.event_logger.info(f"Get key '{key}' from cache")
            self.event_logger.info(self.cache[key])
            return self.cache[key]
        else:
            self.event_logger.warning(f"Key '{key}' not found in cache")
            return None

    @measure_time
    def set(self, key, value):
        if self.re_eval(value):
            if len(self.cache) >= self.max_size:
                self.recycle_memory()
            self.cache[key] = value
            self.event_logger.info(f"Added key '{key}' to cache.")

    @measure_time
    def recycle_memory(self):
        # Implement your memory recycling strategy here
        # Remove oldest item based on date added using lambda function as filter
        oldest_key = min(self.cache, key=lambda x: self.cache[x]['date_added'])
        del self.cache[oldest_key]
        self.event_logger.info(f"Recycled memory by removing key '{oldest_key}' from cache")
        print(self.cache)

    def re_eval(self, value):
        pattern = r'^[a-zA-Z0-9]+$'
        print(value)
        return re.match(pattern, value["value"])        



if __name__ == '__main__':
    # Example usage
    cache = Cache(3)
    for i in range(3):
        current_time = time.perf_counter()
        cache.set(i, {
            "date_added": current_time,
            "value": f"data{i}"
        })
        cache.get(i)

    # Adding new data, which will trigger memory recycling
    cache.set(4, {
        "date_added": current_time,
        "value": "data1"
    })
    print(cache.get(0))  # Output: None (data1 was recycled)
