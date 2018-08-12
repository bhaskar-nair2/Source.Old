import sqlite3 as sql
import datetime
from flask_pymongo import PyMongo

injectionList = ["'", "update", "alter", "select", "delete", "table", "from", "*", ")", ";"]


class SQLConnect:
    def __init__(self):
        self.con = sql.connect('static/datafiles/sourceDB', isolation_level=None)
        self.cur = self.con.cursor()

    def userInsert(self, *args):
        for _ in args:
            _ = self.cleanIt(_)
        q = "insert into users(id,uname,pass,email) values (?,?,?,?)"
        self.cur.execute(q, *args)

    def __getitem__(self, item):
        item = self.cleanIt(item)
        q = "select * from " + item
        rs = self.cur.execute(q)
        return rs.fetchall()

    def addSub(self, item):
        item = self.cleanIt(item)
        q = 'insert into subjects(name, base_code, department) VALUES (?,?,?)'
        self.cur.execute(q, item)
        rs = self.cur.execute('select last_insert_rowid()')
        return rs.fetchone()[0]

    @staticmethod
    def cleanIt(ter):  # TODO:Correct this function and use it!
        for i in injectionList:
            if ter.find(i) == 2:
                ter = ter.replace(i, " ")
                logWrite("sqlslave.cleanIt", " Attack: Type- SQL INJ")
        ter = ter.replace('  ', ' ')
        return ter

    def search(self):
        pass


class MongoConnect:
    def __init__(self, app):
        self.app = app
        self.URI = 'mongodb://127.0.0.1:27017/source-data'
        self.mongo = PyMongo(self.app, self.URI, )
        self.sql = SQLConnect()

    def addUser(self, data):
        client = self.mongo.db['source_credentials']
        rs = client.insert_one(data).inserted_id
        try:
            self.sql.userInsert(rs, data['user'], data['password'], data['mail'])
        except sql.OperationalError:  # TODO add handler for these errors!!
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

def logWrite(module, warning):
    logFile = open('./static/datafiles/log.txt', 'a')
    logFile.write(
        str(datetime.datetime.today()) + " ::" + module + ": {}".format(__name__) + ":: " + warning + "\n")
