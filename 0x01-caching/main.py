
"""
Test
"""
import sys

try:
    LRUCache = __import__('3-lru_cache').LRUCache

    my_cache = LRUCache()
    my_cache.print_cache()
except:
    print(sys.exc_info()[1])