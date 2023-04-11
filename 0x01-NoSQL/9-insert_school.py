#!/usr/bin/env python3
'''Insert a document in Python with mongo_collection as
the pymongo collection object'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a new document in a collection based on kwargs'''
    result = mongo_collection.insert(kwargs)
    return result
