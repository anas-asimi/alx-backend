#!/usr/bin/python3
"""
1-fifo_cache.py
"""
import datetime


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")


class FIFOCache(BaseCaching):
    """FIFOCache
    Args:
        BaseCaching (_type_): _description_
    """

    # def __init__(self):
    #     """ Initiliaze
    #     """
    #     super.__init__()

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
                if self.cache_data.get(oldest_key).get('date') > value.get('date'):
                    oldest_key = key
            del self.cache_data[oldest_key]

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        if self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key).get('value')
