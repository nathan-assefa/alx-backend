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
        self.lru_order = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key and item:
            length = len(self.cache_data)
            if key not in self.cache_data:
                if length >= BaseCaching.MAX_ITEMS:
                    lru_key = self.lru_order.pop()
                    del self.cache_data[lru_key]
                    print("DISCARD:", lru_key)
            else:
                self.lru_order.remove(key)
            self.lru_order.insert(0, key)
            self.cache_data[key] = item
    
    def get(self, key):
        """Getting data from the cache"""
        if key and key in self.cache_data:
            # Move the accessed key to the front of the LRU order
            self.lru_order.remove(key)
            self.lru_order.insert(0, key)
            return self.cache_data[key]
        else:
            return None
