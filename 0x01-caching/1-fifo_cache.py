#!/usr/bin/python3
""" FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching
""" importing the parent class
"""


class FIFOCache(BaseCaching):
    """ FIFO caching method 
        """
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        """ Assign the item to the dictionary 
        """
        if key is None or item is None:
            return
            
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """ deleting first item off the dict
            """
            first_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')
        self.cache_data[key] = item
            
    def get(self, key):
        """ Get an item from the cache by its key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
