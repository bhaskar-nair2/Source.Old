import datetime
import time
import re
from sqlslave import SQLConnect

t1 = "Maths"
t2 = "15SE201J"
t3 = ":teach: Nagalakshmi"

injectionList = ["'", "update", "alter", "select", "delete", "table", "from", "*", ")", ";"]
catList = {"sub": 1, "code": 2, "teach": 3}


class Search:

    def __init__(self, term):
        self.term = str(term).lower()
        self.cleanIt()
        self.cat = self.catIt

    def search(self):
        # TODO:Make sure you only give 8 items as it fucks with the design otherwise
        con=sql.connect('')
        time.sleep(3)
        data = {1: 'hahaha', 2: 'jajajaja', 3: 'kakakaka', 4: 'lololo', 5: 'nanaoonnaa',
                6: 'sjblhasbc lahbcoewfhbi adabhcspiha c', 7: 'hebsc zxfwevbcdahixnjwibefhaj xz',
                8: 'wlehfbhklwefvklhevhklaevhhiqiyhfvivi'}
        return data

    def cleanIt(self):
        ter = self.term
        for i in injectionList:
            if ter.find(i):
                ter = ter.replace(i, " ")
                logWrite("WARNING:: Site Attacked: Type- SQL INJ")
        ter = ter.replace('  ', ' ')
        self.term = ter
        del ter

    @property
    def catIt(self):
        x = re.findall(":(.+?):", self.term)
        if x:
            try:
                return (catList[x])
            except:
                del x
                return 0
        else:
            del x
            return 0

    def terminate(self):
        del self


def logWrite(e):
    logFile = open('./static/datafiles/log.txt', 'a')
    logFile.write(str(datetime.datetime.today()) + "- " + e + "\n")
