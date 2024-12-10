#!/usr/bin/python3


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching method 
        """
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        """ Assign the item to the dictionary 
        """
        if key and item:
            self.cache_data[key] = item
            
        while len(self.cache_data) > BaseCaching.MAX_ITEMS:
            """ deleting first item off the dict
            """
            lst = list(self.cache_data.keys())
            print(lst[0])
            del self.cache_data[lst[0]]
