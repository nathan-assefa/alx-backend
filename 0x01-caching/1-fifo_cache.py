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
        if not key and not item:
            return

        # Check if the key is not precent in the cache_data
        key_not_exist = True if key not in self.cache_data else False

        if len(self.cache_data) >= self.MAX_ITEMS and key_not_exist:
            # first get the first data in the cache
            discard_key = next(iter(self.cache_data))

            # we can also use this method to get the first item in the cache
            # discard_key = next(key for key in self.cache_data)

            # delete the first item
            del self.cache_data[discard_key]

            print("DISCARD: {}".format(discard_key))

        self.cache_data[key] = item

    def get(self, key):
        """Getting data from the cache"""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data[key]
