#!/usr/bin/python3
"""
4-mru_cache.py
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache
    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

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
        already_exist = key in self.cache_data
        if not already_exist and len(self.cache_data) == self.MAX_ITEMS:
            recently_used, value = self.cache_data.popitem(last=True)
            print("DISCARD:", recently_used)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
