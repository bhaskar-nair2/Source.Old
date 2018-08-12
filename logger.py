import datetime


class Logger:
    @staticmethod
    def logWrite(module, warning):
        logFile = open('./static/datafiles/log.txt', 'a')
        logFile.write(str(datetime.datetime.today()) + " ::" +module+ ": {}".format(__name__) + ":: " + warning + "\n")
