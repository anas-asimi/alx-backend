#!/usr/bin/python3
"""
3-lru_cache.py
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache
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
        if len(self.cache_data) + 1 > self.MAX_ITEMS:
            least_used, value = self.cache_data.popitem(last=False)
            print("DISCARD:", least_used)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
