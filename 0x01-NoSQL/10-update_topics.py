#!/usr/bin/env python3
'''Change collection name based on topic names'''


def update_topics(mongo_collection, name, topics):
    '''changes all topics of a school document based on name'''
    item = {"name": name}
    result = {"$set": {"topics": topics}}
    mongo_collection.update_many(item, result)
