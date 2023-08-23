#!/usr/bin/env python3
""" FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """implementing FIFO caching algorithm"""

    def __init__(self):
        """intializing attributes"""
        super().__init__()

    def put(self, key, item):
        """Inserting data to the cache"""
        if key and item:
            length = len(self.cache_data)

            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                fifo_key = next(iter(self.cache_data.keys()))
                del self.cache_data[fifo_key]
                print("DISCARD: {}".format(fifo_key))

            self.cache_data[key] = item

    def get(self, key):
        """Getting data from the cache"""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data[key]
