#!/usr/bin/env python3
"""
a function that list all topics that match
"""


def schools_by_topic(mongo_collection, topic):
    """
    Args:
    mongo_collection - the collection
    topic - topic to match
    """

    sch_list = mongo_collection.find({"topics:" topic})
    return [school for school in sch_list]
