from flask_pymongo import PyMongo
import json
import datetime
import sqlslave


# db = source-data
# collections = [source_credentials, ]

class MongoConnect:
    def __init__(self, app):
        self.app = app
        self.URI = 'mongodb://127.0.0.1:27017/source-data'
        self.mongo = PyMongo(self.app, self.URI, )
        self.sql = sqlslave.SQLConnect()

    def addUser(self, data):
        client = self.mongo.db['source_credentials']
        rs = client.insert_one(data).inserted_id
        try:
            self.sql.userInsert(rs, data['user'], data['password'], data['mail'])
        except sqlslave.sql.OperationalError:  # TODO add handler for these errors!!
            logWrite('Insert to SQL failed by MongoConnect.insert')
            pass

    def checkUser(self, st):
        client = self.mongo.db['source_credentials']
        re = client.find_one({"user": str(st)})
        if re is None:
            return True
        else:
            return False

    def getUser(self, st):
        if self.checkUser(st):
            client = self.mongo.db['source_credentials']
            re = client.find_one({"user": str(st)})
            return re
        else:
            return False

    def addSub(self, item):
        client = self.mongo.db['subjects']
        client.insert_one(item)

    def subdesc(self, item):
        client = self.mongo.db['subjects']
        re = client.find_one({"sub_id": item})
        return re
