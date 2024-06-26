#!/usr/bin/python3
'''
A class that inherits from BaseCaching and is a caching system
'''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    Inherits from Basecaching class
    Attributes:
        put - method that adds a key/value pair to cache
        get - method that retrieves a key/value pair from cache
    '''

    def put(self, key, item):
        '''Adds key/value pair to cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Return value stored in cache with key of value'''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
