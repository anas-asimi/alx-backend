#!/usr/bin/python3
"""
1-fifo_cache.py
"""
import datetime
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache
    Args:
        BaseCaching (_type_): _description_
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return None
        self.cache_data[key] = {
            'value': item,
            'date': datetime.datetime.now()
        }
        if len(self.cache_data) > self.MAX_ITEMS:
            oldest_key = None
            for key, value in self.cache_data.items():
                if oldest_key is None:
                    oldest_key = key
                if self.cache_data[oldest_key]['date'] > value['date']:
                    oldest_key = key
            print("DISCARD:", oldest_key)
            del self.cache_data[oldest_key]

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key).get('value')
