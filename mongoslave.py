from flask_pymongo import PyMongo
import sqlslave

class MongoConnect:
    def __init__(self, app):
        self.app = app
        self.URI = 'mongodb://mongoslaveuser:mongoslave123@ds141221.mlab.com:41221/source-data'
        self.mongo = PyMongo(self.app,self.URI,)

    def insert(self,collection,data):
        client = self.mongo.db[collection]
        rs = client.insert_one(data).inserted_id





