#!/usr/bin/env python3
""" LFU caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines an LFU caching system"""

    def __init__(self):
        """Initialize the LFUCache"""
        super().__init__()
        # To track the frequency of each key
        self.frequency = {}
        # To maintain the order of usage for each frequency
        self.lfu_order = {}

    def put(self, key, item):
        """Cache a key-value pair"""
        if key is not None and item is not None:
            key_not_exist = True if key not in self.cache_data else False
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key_not_exist:
                # Find the least frequency used item
                min_freq = min(self.lfu_order)
                # Remove the least frequency used key
                lfu_key = self.lfu_order[min_freq].pop(0)

                if not self.lfu_order[min_freq]:
                    del self.lfu_order[min_freq]

                # Delete the corresponding key from the cache
                del self.cache_data[lfu_key]
                # Delete the frequency record
                del self.frequency[lfu_key]
                print("DISCARD:", lfu_key)

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

            # Add the key-value pair to the cache
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to a given key, or None"""
        if key in self.cache_data:
            # Update the frequency and usage order for the accessed key
            freq = self.frequency[key]
            self.frequency[key] = freq + 1
            self.lfu_order[freq].remove(key)

            if freq + 1 in self.lfu_order:
                self.lfu_order[freq + 1].append(key)
            else:
                self.lfu_order[freq + 1] = [key]

            return self.cache_data[key]
        else:
            return None
