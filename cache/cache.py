class Cache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return None

    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            self.recycle_memory()
        self.cache[key] = value

    def recycle_memory(self):
        # Implement your memory recycling strategy here
        # For simplicity, let's just remove the oldest item
        oldest_key = next(iter(self.cache))
        del self.cache[oldest_key]


if __name__ == '__main__':
    # Example usage
    cache = Cache(max_size=3)
    cache.set(1, "data1")
    cache.set(2, "data2")
    cache.set(3, "data3")

    print(cache.get(1))  # Output: data1
    print(cache.get(2))  # Output: data2
    print(cache.get(3))  # Output: data3

    # Adding new data, which will trigger memory recycling
    cache.set(4, "data4")

    print(cache.get(1))  # Output: None (data1 was recycled)
