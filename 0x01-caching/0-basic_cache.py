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
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        dic = self.cache_data
    
    
    def put(self, key, item):
        """ return updated dict
        """
        if key == None or item == None:
            pass
        else:
            return self.cache_data.update({key: item})
    def get(self, key):
        """ check dict for specific key
        """
        if key == None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get('key')
