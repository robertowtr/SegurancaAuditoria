#!/usr/bin/python
from time import *
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

data = bytearray("a")
endereco = bytearray("cd7004x0")
print data


def x():
    while 1:
        print "%s-%s-%s %s:%s:%s\tEnviando broadcast..." % localtime()[:6]
        data.append(1)
        s.sendto(data, ('localhost', 32000))
        #sleep(0.1)

        recebido, addr = s.recvfrom(1024)
        print "Recebido %s" % recebido + " len: " + str(len(recebido))


x()