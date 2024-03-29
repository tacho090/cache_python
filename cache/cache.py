from cache_log.log import MyLogger
import time
from helpers import measure_time, measure_memory, MEMORY_THRESHOLD_MB, re_eval


class Cache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = {}
        self.event_logger = MyLogger('event_logger', 'event_logger.log')
        self.time_logger = MyLogger('time_logger', 'time_logger.log')
        self.memory_logger = MyLogger('memory_logger', 'memory_logger.log')
        self.memory_logger.info("Start memory logger")
        self.memory_logger.info(f"70% of total available memory in MB: {MEMORY_THRESHOLD_MB}")
        self.event_logger.info("Start event logger")
        self.time_logger.info("Start time logger")


    @measure_time
    @measure_memory
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
        if re_eval(value):
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
