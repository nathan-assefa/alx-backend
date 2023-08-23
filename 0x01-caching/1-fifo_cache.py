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
            pass

        # Check if the key is not precent in the cache_data
        key_not_exist = True if key not in self.cache_data else False
        
        if key_not_exist:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discard_key = next(iter(self.cache_data))
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))

        else:
            del self.cache_data[key]

        self.cache_data[key] = item

        '''
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
        '''

    def get(self, key):
        """Getting data from the cache"""
        if not key or key not in self.cache_data:
            return None

        return self.cache_data[key]
