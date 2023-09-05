#!/usr/bin/env python3
"""Returns a list with all school documents having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list with all school documents having a specific topic"""
    return mongo_collection.find({"topics": topic})
