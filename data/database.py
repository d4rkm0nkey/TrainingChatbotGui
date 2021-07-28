import os
import enum
import pymongo
from pymongo.errors import OperationFailure

class Database(object):
    DATABASE = None
    class COLLECTIONS():
        BOT = "bot"
        SENTENCE = "sentence"
        CATEGORY = "category"
        EMOTION = "emotion"
        DOMAIN = "domain"

    @staticmethod
    def initialize():
        try:
            client = pymongo.MongoClient(os.getenv("DATABASE_IP"),
                                        username=os.getenv("DATABASE_USERNAME"),
                                        password=os.getenv("DATABASE_PASSWORD"),
                                        authSource='chatbot')
            Database.DATABASE = client["chatbot"]
            try:
                client.server_info()
            except OperationFailure as e:
                print(e)
                raise e
        except Exception as e:
            print(e)
            raise e

    @staticmethod
    def insert(collection, data):
        return Database.DATABASE[collection].insert_one(data).inserted_id

    @staticmethod
    def replace(collection, data):
        return Database.DATABASE[collection].replace_one({"_id": data["_id"]}, data)

    @staticmethod
    def contains(collection, query):
        return Database.DATABASE[collection].count_documents(query)

    @staticmethod
    def delete_all(collection):
        Database.DATABASE[collection].drop()

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def delete_one(collection, query):
        return Database.DATABASE[collection].delete_one(query)

    @staticmethod
    def delete_many(collection, query):
        return Database.DATABASE[collection].delete_many(query)
