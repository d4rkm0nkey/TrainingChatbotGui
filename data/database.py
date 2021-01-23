import os
import enum
import pymongo

class Database(object):
    DATABASE = None
    class COLLECTIONS():
        SENTENCE = "sentence"
        CATEGORY = "category"
        EMOTION = "emotion"

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(os.getenv("DATABASE_IP"),
                                    username=os.getenv("DATABASE_USERNAME"),
                                    password=os.getenv("DATABASE_PASSWORD"),
                                    authSource='chatbot')
        Database.DATABASE = client["chatbot"]

    @staticmethod
    def insert(collection, data):
        return Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def replace(collection, data):
        return Database.DATABASE[collection].replace_one({"_id": data["_id"]}, data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def delete_one(collection, query):
        return Database.DATABASE[collection].delete_one(query)
