#!/usr/bin/python3
""" MRUCache module
"""

from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching
""" importing the parent class
"""


class MRUCache(BaseCaching):
    """ MRU caching method
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        
    def put(self, key, item):
        """ check if key and item exists and proceed with
            MRU algo
        """
        if key is None or item is None:
            return

        
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """ deleting the recent used item off the dict
                """
                del_key, del_item = self.cache_data.popitem(last=True)
                print(f'DISCARD: {del_key}')
        
        self.cache_data[key] = item
            
    def get(self, key):
        """ Get an item from the cache by its key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data[key] = item
        return self.cache_data[key]
