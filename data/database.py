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
        Database.DATABASE[collection].insert(data.__dict__)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
