import hashlib
class Hasher:
    def __init__(self,username,password):
        self.username=username
        self.hash=self.get_hash(password)


    def get_hash(self,password):
        for _ in range(0,9999999):
            head=(str(_)+self.username+password).encode()
            i=hashlib.sha3_256(head).hexdigest()
            if(i[:4]=='0000'):
                self.num=_
                return i

    @staticmethod
    def retrive(val,password):
        head = (str(val['num']) + val['name'] + password).encode()
        i = hashlib.sha3_256(head).hexdigest()
        if i==val['hash']:
            return True
        else:
            return False

    def maker(self):
        arr = {"hash": self.hash, "num": self.num}
        return arr

    # Others are just for demo, Use this method for work
    @staticmethod
    def build(username, password, salt):
        head = (str(salt) + username + password).encode()
        i = hashlib.sha3_256(head).hexdigest()
        return [username, i]

# secret_key = b"\xd0\t\xc4#lM`2;c\x14T3^\x02\xd7y\x81wYouKnowWhat?JustFuckOff"
# print(Hasher.build('bhaskar', 'bbnair', secret_key))

