from flask_pymongo import PyMongo
import datetime
import sqlslave


class MongoConnect:
    def __init__(self, app):
        self.app = app
        self.URI = 'mongodb://127.0.0.1:27017/source-data'
        self.mongo = PyMongo(self.app, self.URI, )
        self.sql = sqlslave.SQLConnect()

    def insert(self, collection, data):
        client = self.mongo.db[collection]
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


x = "streak"


class MongoFiles():
    def f1(self):
        pass


def logWrite(e):
    logFile = open('./static/datafiles/log.txt', 'a')
    logFile.write(str(datetime.datetime.today()) + "- " + e + "\n")
