#!/usr/bin/python3
""" FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching
""" importing the parent class
"""


class LIFOCache(BaseCaching):
    """ LIFO caching method
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ check if key and item exists and proceed with
            LIFO algo
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """ deleting last item off the dict
            """
            last_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(last_key)
            print(f'DISCARD: {last_key}')
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by its key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
