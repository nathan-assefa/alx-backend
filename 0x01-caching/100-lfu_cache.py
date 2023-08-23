#!/usr/bin/env python3
""" LFU caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines an LFU caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.usage_order = []  # To maintain the order of usage
        self.key_frequency = {}  # To track the frequency of each key

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            return

        cache_size = len(self.cache_data)
        if cache_size >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            min_frequency = min(self.key_frequency.values())
            least_frequent_keys = [
                k for k, v in self.key_frequency.items() if v == min_frequency
            ]

            if len(least_frequent_keys) > 1:
                lru_least_frequent = {
                    k: self.usage_order.index(k) for k in least_frequent_keys
                }
                discard_key = min(
                        lru_least_frequent, key=lru_least_frequent.get
                        )
            else:
                discard_key = least_frequent_keys[0]

            print("DISCARD:", discard_key)
            del self.cache_data[discard_key]
            self.usage_order.remove(discard_key)
            del self.key_frequency[discard_key]

        if key in self.key_frequency:
            self.key_frequency[key] += 1
        else:
            self.key_frequency[key] = 1

        if key in self.usage_order:
            self.usage_order.remove(key)

        self.usage_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            self.key_frequency[key] += 1
            return self.cache_data[key]
        return None
