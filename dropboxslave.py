import dropbox


# Drop box Oath2: W7_kDDrfizAAAAAAAAABARUJ3DwXYPp7YdfYTPyAFUUK6J3Gu3X5-qZzOJwrEv5k

class dxConnect():
    def __init__(self):
        self.dbx = dropbox.Dropbox('W7_kDDrfizAAAAAAAAABARUJ3DwXYPp7YdfYTPyAFUUK6J3Gu3X5-qZzOJwrEv5k')
        print(self.dbx.users_get_current_account())

    def upload(self):
        with open("static/img/favicon.ico", "rb") as f:
            self.dbx.files_upload(f.read(), f.name, mute=True)


if __name__ == '__main__':
    dc = dxConnect()
    dc.upload()
