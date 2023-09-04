#!/usr/bin env python3
"""Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a colection.
    Returns "[]" if collection is empty
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    return mongo_collection.find()
