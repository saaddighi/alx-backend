
"""
Test
"""
import sys

try:
    MRUCache = __import__('4-mru_cache').MRUCache
    from base_caching import BaseCaching

    BaseCaching.MAX_ITEMS = 5
    MRUCache.MAX_ITEMS = 5
    my_cache = MRUCache()
    my_cache.MAX_ITEMS = 5
    
    for i in range(10):
        key = "key-{}".format(i)
        value = "value-{}".format(i)
        my_cache.put(key, value)
        my_cache.get(key)
        my_cache.print_cache()
    
    my_cache.get("key-0")
    my_cache.get("key-4")
    my_cache.get("key-6")
    my_cache.get("key-7")
    my_cache.print_cache()
    my_cache.put("key-20", "value-20")
    my_cache.put("key-21", "value-21")
    my_cache.put("key-22", "value-22")
    my_cache.print_cache()

except:
    print(sys.exc_info()[1])