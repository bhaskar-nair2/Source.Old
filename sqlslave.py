import sqlite3 as sql
import datetime
from logger import Logger

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
                Logger.logWrite("sqlslave.cleanIt", " Attack: Type- SQL INJ")
        ter = ter.replace('  ', ' ')
        return ter

    def search(self):
        pass

