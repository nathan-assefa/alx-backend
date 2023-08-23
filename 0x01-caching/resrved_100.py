#!/usr/bin/env python3
""" LFU caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item
            
            # Update the frequency of the key
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.evict_least_frequent()

    def get(self, key):
        if key in self.cache_data:
            self.update_frequency(key)
            return self.cache_data[key]
        else:
            return None
    
    def evict_least_frequent(self):
        min_freq = min(self.frequency.values())
        lfu_keys = [key for key, freq in self.frequency.items() if freq == min_freq]
        
        if len(lfu_keys) > 1:
            self.evict_least_recent(lfu_keys)  # Use LRU algorithm for ties
        else:
            lfu_key = lfu_keys[0]
            self.remove_key(lfu_key)
            print("DISCARD:", lfu_key)

    def update_frequency(self, key):
        self.frequency[key] += 1
    
    def evict_least_recent(self, keys):
        lru_key = min(keys, key=lambda k: self.cache_data[k][1])  # LRU tie-breaker
        self.remove_key(lru_key)
        print("DISCARD:", lru_key)
    
    def remove_key(self, key):
        del self.cache_data[key]
        del self.frequency[key]
