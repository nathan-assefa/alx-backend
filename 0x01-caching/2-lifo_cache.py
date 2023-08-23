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
            return
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

        '''
         key_not_exist = True if key not in self.cache_data else False

        if key_not_exist:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discard_key = next(iter(reversed(self.cache_data)))
                # or we can use this
                # last_key = list(self.cache_data.keys())[-1]

                del self.cache_data[discard_key]

                print("DISCARD: {}".format(discard_key))

        else:
            # If the value is not None, indicating an existing key, it deletes
            # +the existing key-value pair from the cache before updating it.
            del self.cache_data[key]

        self.cache_data[key] = item
        '''

    def get(self, key):
        """Getting data from the cache"""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
