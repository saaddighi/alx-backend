from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements
        the Most Recently Used (MRU) caching system
    """

    def __init__(self):
        """ Initialize the MRUCache instance """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
            - If key or item is None, do nothing
            - If the cache exceeds MAX_ITEMS, discard the most recently used item
        """
        if key is None or item is None:
            return
        
        # If the key already exists, remove it to update the order
        if key in self.cache_data:
            del self.cache_data[key]
        
        # Add the item to the cache, and it becomes the most recently used
        
        # Check if the number of items exceeds the MAX_ITEMS limit
        if key not in self.cache_data:    
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # The most recently used item is the last item in OrderedDict
            
                mru_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item
        
            

    def get(self, key):
        """ Get an item by key
            - Return None if the key doesn't exist or is None
        """
        if key is None or key not in self.cache_data:
        
            return None
        # Move the accessed item to the end to mark it as most recently used
        self.cache_data[key] = item
        return self.cache_data[key]
