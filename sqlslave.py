import sqlite3 as sql
import datetime


class SQLConnect:
    def __init__(self):
        self.con = sql.connect('static/datafiles/sourceDB')
        self.cur = self.con.cursor()

    def userInsert(self, *args):
        q = "insert into users(id,uname,pass,email) values (?,?,?,?)"
        self.cur.execute(q, *args)


def logWrite(e):
    logFile = open('./static/datafiles/log.txt', 'a')
    logFile.write(str(datetime.datetime.today()) + "- " + e + "\n")