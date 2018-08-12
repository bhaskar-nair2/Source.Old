import re
from sqlslave import SQLConnect
from logger import Logger

t1 = "Maths"
t2 = "15SE201J"
t3 = ":teach: Nagalakshmi"

catList = {'sub': 1, 'code': 2, 'teach': 3, 'file': 4}


class Search:

    def __init__(self, term):
        self.term = str(term).lower()
        self.cat = self.catIt

    @property
    def catIt(self):
        x = re.findall(":(.+?):", self.term)
        print(self.term)
        # self.term = re.sub(":(.+?):", self.term, '')
        if x:
            try:
                return (catList[x])
            except:
                del x
                return 0
        else:
            del x
            return 0

    def search(self):
        print(self.term)
        # TODO:Make sure you only give 8 items as it fucks with the design otherwise
        data = {1: 'hahaha', 2: 'jajajaja', 3: 'kakakaka', 4: 'lololo', 5: 'nanaoonnaa',
                6: 'sjblhasbc lahbcoewfhbi adabhcspiha c', 7: 'hebsc zxfwevbcdahixnjwibefhaj xz',
                8: 'wlehfbhklwefvklhevhklaevhhiqiyhfvivi'}
        return data

    def terminate(self):
        del self
