#!/usr/bin/env python3
'''A function that returns the list of schools having a specific topic'''


def schools_by_topic(mongo_collection, topic):
    result = mongo_collection.find({"topic": topic})
    return list(result)
