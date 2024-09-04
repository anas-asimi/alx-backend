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
            key_to_discard = None
            elements_never_used = [
                k for k in self.cache_data.keys() if k not in self.get_history]
            if len(elements_never_used) > 0:
                for k in self.cache_data.keys():
                    if k in elements_never_used:
                        key_to_discard = k
                        break

            else:
                frequently_used_keys = [
                    k for k in self.get_history if k in self.cache_data]
                frequently_used_keys_counted = Counter(
                    frequently_used_keys)
                lowest_number = list(
                    frequently_used_keys_counted.values())[0]
                for k in self.cache_data.keys():
                    if frequently_used_keys_counted.get(k) == lowest_number:
                        key_to_discard = k
                        break

            self.cache_data.pop(key_to_discard)
            print("DISCARD:", key_to_discard)

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.get_history.append(key)
        return self.cache_data.get(key)
