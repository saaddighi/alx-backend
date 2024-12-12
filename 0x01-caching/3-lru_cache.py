#!/usr/bin/python3
""" LRUCache module
"""

from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching
""" importing the parent class
"""


class LRUCache(BaseCaching):
    """ LRU caching method
    """
    def __init__(self):
        super().__init__()
        

    def put(self, key, item):
        """ check if key and item exists and proceed with
            LRU algo
        """
        self.cache_data = OrderedDict(self.data_cache)
        if key is None or item is None:
            return

        elif key in self.cache_data:
            self.ordrdict.move_to_end(key)
            
        self.cache_data[key]
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            """ deleting the least used item off the dict
            """
            del_key, del_item = self.cache_data.popitem(last=False)
            print(f'DISCARD: {del_key}')


    def get(self, key):
        """ Get an item from the cache by its key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]