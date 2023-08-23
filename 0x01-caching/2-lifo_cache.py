#!/usr/bin/env python3
""" LIFO caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """implementing LIFO caching algorithm"""

    def __init__(self):
        """intializing attributes"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            if key in self.order:
                del self.order[self.order.index(key)]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Getting data from the cache"""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
