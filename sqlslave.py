import sqlite3 as sql


class Slave:
    def __init__(self):
        self.con = sql.connect('static/datafiles/sourceDB')
        self.cur = self.con.cursor()

    def UserInsert(self, *args):
        q = "insert into users(uname,pass) values (?,?)"
        self.cur.execute(q, *args)

