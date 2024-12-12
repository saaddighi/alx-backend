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
        self.ordrdict = OrderedDict(self.data_cache)

    def put(self, key, item):
        """ check if key and item exists and proceed with
            LRU algo
        """
        if key is None or item is None:
            self.ordrdict.move_to_end(key)

        elif len(self.ordrdict) > BaseCaching.MAX_ITEMS:
            """ deleting the least used item off the dict
            """
            self.ordrdict.popitem(last=False)

    self.ordrdict[key]

    def get(self, key):
        """ Get an item from the cache by its key
        """
        if key is None or key not in self.ordrdict:
            return None
        return self.ordrdict[key]
