#!/usr/bin/env python3
""" MRU caching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """implementing MRU caching algorithm"""

    def __init__(self):
        """intializing attributes"""
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """Inserting data to the cache"""
        if key or item is not None:
            key_not_exist = True if key not in self.cache_data else False
            if key_not_exist:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Discard the most recently used item
                    mru_key = self.mru_order.pop(0)
                    del self.cache_data[mru_key]
                    print("DISCARD:", mru_key)

            else:
                del self.cache_data[key]

            if key in self.mru_order:
                self.mru_order.remove(key)

            self.mru_order.insert(0, key)

            self.cache_data[key] = item

    def get(self, key):
        """Getting data from the cache"""
        if key in self.cache_data:
            # Move the accessed key to the front of the MRU order
            self.mru_order.remove(key)
            self.mru_order.insert(0, key)
            return self.cache_data[key]
        else:
            return None
