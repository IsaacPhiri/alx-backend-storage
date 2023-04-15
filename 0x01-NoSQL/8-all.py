#!/usr/bin/env python3
""" a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """List all documents
    Arguments:
    mongo_collection: the pymongo collection object to list the
    documents from
    Returns:
    a list of dictionaries representing each document in the collection
    """

    pointer = mongo_collection.find({})
    documents = list(pointer)
    return documents
