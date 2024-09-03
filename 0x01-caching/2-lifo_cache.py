#!/usr/bin/python3
"""
2-lifo_cache.py
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache
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
        if len(self.cache_data) == self.MAX_ITEMS:
            last_key, value = self.cache_data.popitem(last=True)
            print("DISCARD:", last_key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key, None)
