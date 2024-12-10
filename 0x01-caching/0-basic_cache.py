#!/usr/bin/python3
    
BaseCaching = __import__('base_caching').BaseCaching    


class BasicCache(BaseCaching):
    
    def __init__(self):
        super().__init__()
        dic = self.cache_data
    
    
    def put(self, key, item):
        if key == None or item == None:
            pass
        else:
            return self.cache_data.update({key: item})
    def get(self, key):
        
        if key == None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get('key')
            
            