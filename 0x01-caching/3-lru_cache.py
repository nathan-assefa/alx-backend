#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """
    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key and item:
            length = len(self.cache_data)
            if key not in self.cache_data:
                if length >= BaseCaching.MAX_ITEMS:
                    lru_key = self.usage.pop()
                    del self.cache_data[lru_key]
                    print("DISCARD:", lru_key)
            else:
                self.usage.remove(key)
            self.usage.insert(0, key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            self.usage.remove(key)
            self.usage.insert(0, key)
            return self.cache_data[key]
        return None
