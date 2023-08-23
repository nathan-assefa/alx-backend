#!/usr/bin/env python3
""" FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """implementing FIFO caching algorithm"""

    def __init__(self):
        """intializing attributes"""
        super().__init__()

    def put(self, key, item):
        """
            modify cache data

            Args:
                key: of the dict
                item: value of the key
        """
        if key or item is not None:
            valuecache = self.get(key)
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = list(self.cache_data.keys())[0]
                    del self.cache_data[keydel]
                    print("DISCARD: {}".format(keydel))

            self.cache_data[key] = item


    def get(self, key):
        """Getting data from the cache"""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data[key]
