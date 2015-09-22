#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adrian
#
# Created:     22/09/2015
# Copyright:   (c) Adrian 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import socket
class GameSocket:

    ip = ""
    received_data = []

    def startGame(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((socket.gethostname(), 80))
        serversocket.listen(1)
        conn, addr = serversocket.accept()
        print('Connected ' + addr)
        while 1:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
        conn.close()

    def getAnswers():
        return received_data

    def setAnswers(data):
        received_data = data

