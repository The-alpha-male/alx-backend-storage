# #!/usr/bin/env python3

# def update_topics(mongo_collection, name, topics):
#     """Change all topics of the school doc based on the name arg
#     args:
#     mongo_collection: collection to update
#     name: name of the school to update
#     @topics: list to update
#     """
#     mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

#!/usr/bin/env python3
"""
a Python function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
