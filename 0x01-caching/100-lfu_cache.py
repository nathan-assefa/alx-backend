#!/usr/bin/env python3
""" LFU caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """implementing LFU caching algorithm"""

    def __init__(self):
        """intializing attributes"""
        super().__init__()
        self.frequency = {}  # To track the frequency of each key
        self.lfu_order = {}

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item  # Add the key-value pair to the cache

            # Update the frequency of the key and its usage order
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            freq = self.frequency[key]

            if freq in self.lfu_order:
                self.lfu_order[freq].append(key)
            else:
                self.lfu_order[freq] = [key]

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequency used item
                min_freq = min(self.lfu_order)
                lfu_key = self.lfu_order[min_freq].pop(
                    0
                )  # Remove the least frequency used key

                if not self.lfu_order[min_freq]:
                    del self.lfu_order[min_freq]

                del self.cache_data[
                    lfu_key
                ]  # Delete the corresponding key from the cache
                del self.frequency[lfu_key]  # Delete the frequency record
                print("DISCARD:", lfu_key)

    def get(self, key):
        if key in self.cache_data:
            # Update the frequency and usage order for the accessed key
            freq = self.frequency[key]
            self.frequency[key] = freq + 1
            self.lfu_order[freq].remove(key)

            if freq + 1 in self.lfu_order:
                self.lfu_order[freq + 1].append(key)
            else:
                self.lfu_order[freq + 1] = [key]

            return self.cache_data[key]  # Return the value associated with the key
        else:
            return None
