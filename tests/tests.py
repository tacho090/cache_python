import unittest
from cache.cache import Cache

class TestCache(unittest.TestCase):
    def test_cache_get(self):
        cache = Cache(max_size=3)
        cache.set(1, "data1")
        cache.set(2, "data2")
        cache.set(3, "data3")

        self.assertEqual(cache.get(1), "data1")
        self.assertEqual(cache.get(2), "data2")
        self.assertEqual(cache.get(3), "data3")
        self.assertIsNone(cache.get(4))  # Key not present in cache

    def test_cache_set(self):
        cache = Cache(max_size=2)
        cache.set(1, "data1")
        cache.set(2, "data2")
        cache.set(3, "data3")  # Trigger memory recycling

        self.assertIsNone(cache.get(1))  # data1 should be recycled
        self.assertEqual(cache.get(2), "data2")
        self.assertEqual(cache.get(3), "data3")

    def test_cache_recycle_memory(self):
        cache = Cache(max_size=2)
        cache.set(1, "data1")
        cache.set(2, "data2")
        cache.set(3, "data3")  # Trigger memory recycling

        self.assertNotIn(1, cache.cache)  # data1 should be recycled
        self.assertIn(2, cache.cache)
        self.assertIn(3, cache.cache)

if __name__ == '__main__':
    unittest.main()
