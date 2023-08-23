#!/usr/bin/env python3
""" Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implementing basic caching algorithm"""

    def put(self, key, item):
        """inseting data into the cache"""
        if key or item is not None:
            self.cache_data[key] = item
    
    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
