#!/usr/bin/env python3
""" Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implementing basic caching algorithm"""

    def put(self, key, item):
        """inseting data into the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Getting data from the cache"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
