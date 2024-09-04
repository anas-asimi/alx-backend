#!/usr/bin/python3
"""
100-lfu_cache.py
"""

from collections import Counter, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache
    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.get_history = []

    def print_cache_ordered(self):
        """Prints the cache ordered.
        """
        print("Current cache:")
        for key in self.cache_data.keys():
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return None

        if key not in self.cache_data \
                and len(self.cache_data) == self.MAX_ITEMS:
            LENGTH = 10
            frequently_used_keys = [
                k for k in self.get_history if k in self.cache_data]

            if any(k not in frequently_used_keys
                   for k in self.cache_data.keys()):
                for k in self.cache_data.keys():
                    if k not in frequently_used_keys:
                        self.cache_data.pop(k)
                        print("DISCARD:", k)
                        break
            else:
                frequently_used_keys_counted = Counter(frequently_used_keys)
                lowest_number = list(frequently_used_keys_counted.values())[0]

                for k in self.cache_data.keys():
                    if frequently_used_keys_counted.get(k) == lowest_number \
                            or k not in frequently_used_keys:
                        self.cache_data.pop(k)
                        print("DISCARD:", k)
                        break
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.get_history.append(key)
            if len(self.get_history) == 10:
                self.get_history.pop(0)
        return self.cache_data.get(key)
