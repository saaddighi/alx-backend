#!/usr/bin/python3
""" BaseCaching module
"""

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
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
    
    
class BasicCache(BaseCaching):
    
    dic = self.cache_data
    
    def put(self, key, item):
        if key == None or item == None:
            pass
        else:
            return dic.update({key: item})
    def get(self, key):
        
        if key == None or key not in dic:
            return None
        else:
            return dic.key('key')
            
            