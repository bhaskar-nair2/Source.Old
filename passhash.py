import hashlib


class Hasher:
    def __init__(self, username, password):
        self.username = username
        self.hash = self.get_hash(password)

    def get_hash(self, password):
        for _ in range(0, 9999999):
            head = (str(_) + self.username + password).encode()
            i = hashlib.sha3_256(head).hexdigest()
            if (i[:4] == '0000'):
                self.num = _
                return i

    def maker(self):
        arr = {"hash": self.hash, "num": self.num}
        return arr

    # Others are just for demo, Use these methods for work
    @staticmethod
    def build(username, password, salt):
        head = (str(salt) + username + password).encode()
        i = hashlib.sha3_256(head).hexdigest()
        return [username, i]

    @staticmethod
    def retrive(uname, password, salt, val):
        head = (str(salt) + uname + password).encode()
        i = hashlib.sha3_256(head).hexdigest()
        if i == val:
            return True
        else:
            return False
