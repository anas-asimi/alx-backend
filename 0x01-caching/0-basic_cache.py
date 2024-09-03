#!/usr/bin/python3
"""
0-basic_cache.py
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    Args:
        BaseCaching (_type_): _description_
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
