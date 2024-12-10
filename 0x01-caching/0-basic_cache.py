#!/usr/bin/python3
""" BasicCache module
"""    

BaseCaching = __import__('base_caching').BaseCaching
""" importing the parent class
"""    


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - method to update the dict
      - method to check if key in in the dict
    """
    
    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value associated with the given key """
        return self.cache_data.get(key)
