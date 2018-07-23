import sqlite3 as sql
import datetime

injectionList = ["'", "update", "alter", "select", "delete", "table", "from", "*", ")", ";"]


class SQLConnect:
    def __init__(self):
        self.con = sql.connect('static/datafiles/sourceDB')
        self.cur = self.con.cursor()

    def userInsert(self, *args):
        q = "insert into users(id,uname,pass,email) values (?,?,?,?)"
        self.cur.execute(q, *args)

    def cleanIt(self):  # TODO:Correct this function and use it!
        ter = self.term
        for i in injectionList:
            if ter.find(i):
                ter = ter.replace(i, " ")
                logWrite("WARNING:: Site Attacked: Type- SQL INJ")
        ter = ter.replace('  ', ' ')
        self.term = ter
        del ter


def logWrite(e):
    logFile = open('./static/datafiles/log.txt', 'a')
    logFile.write(str(datetime.datetime.today()) + "- " + e + "\n")
