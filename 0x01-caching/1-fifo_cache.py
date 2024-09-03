#!/usr/bin/python3
"""
1-fifo_cache.py
"""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache
    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return None
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_key, value = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key).get('value')
