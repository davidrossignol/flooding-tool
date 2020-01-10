import os

class Target():
    def __init__(self, host, port=0):
        self.host = host
        self.port = port

    def isAlive(self):
        res = os.system("ping -c 1 " + self.host)
        if res == 0:
            print("Host %s is up!" % (self.host))
            return True
        else:
            print("Host %s is down!" % (self.host))
            return False