import pymongo

client = pymongo.MongoClient('mongodb://localhost/tutorial_bot')
users_db = client.get_database()["users_db"]
