#!/usr/bin/env python3
""" LRU caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """implementing LRU caching algorithm"""

    def __init__(self):
        """intializing attributes"""
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """Inserting data to the cache"""

        if key and item:
            key_not_exist = True if key not in self.cache_data else False
            if key_not_exist:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Discard the least recently used item
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
