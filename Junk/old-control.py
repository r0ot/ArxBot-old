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

#(2,24)
old_setting = WConio.gettextinfo()[4] & 0x00FF
WConio.clrscr()
WConio.settitle("PyBot Control Center")
WConio.gotoxy(2,2)
WConio.cputs("Welcome to the PyBot Control Center\n\r")
f = open('C:\\PyBot\\connections.txt', 'w')
j = open('C:\\PyBot\\update.txt', 'w')
p = open('C:\\PyBot\\cmd.txt', 'w')
f.write('')
j.write('')
p.write('')
f.close()
j.close()

class GetConnections ( threading.Thread ):
    def run ( self ):
	WConio.textcolor(WConio.LIGHTRED)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = ''
	port = 8888
	s.bind((host, port))
	s.listen(1)
	IPs = []
	WConio.gotoxy(0,25)
	WConio.cputs("Awaiting Connections...")
	WConio.gotoxy(19,23)
	while 1:
            conn, addr = s.accept()
            WConio.gotoxy(0,25)
            WConio.cputs("Connection Recieved -- Adding to File")
	    WConio.gotoxy(19,23)
	    f = open('C:\\PyBot\\connections.txt', 'a')
	    f.write(addr[0] + '\n')
	    f.close()

class UpdateOnlines ( threading.Thread ):
    def run ( self ):
        WConio.textcolor(WConio.LIGHTGREEN)
        IPs = []
        time.sleep(1)
        while 1:
	    r = open('C:\\PyBot\\connections.txt', 'r')
	    str = r.read().split("\n")
	    r.close()
	    for i in str:
	    	if i != '':
                    try:
			IPs.index(i)
                    except:
			IPs.append(i)
            f = open('C:\\PyBot\\update.txt', 'w')
            x = WConio.wherex()
            y = WConio.wherey()
            for st in IPs:
                f.write(st + '\n')
		WConio.gotoxy(0,4)
		WConio.cputs(st + '\n\r')
            f.close()
            WConio.gotoxy(x, y)
            time.sleep(2)
			
class GetCommands ( threading.Thread ):
    def run ( self ):
        WConio.textcolor(WConio.LIGHTCYAN)
        while 1:
            WConio.gotoxy(79, 1)
            WConio.cputs(" ")
            WConio.gotoxy(78, 2)
            WConio.cputs(" ")
            WConio.gotoxy(77, 3)
            WConio.cputs(" ")
            WConio.gotoxy(76, 4)
            WConio.cputs(" ")
            WConio.gotoxy(2,23)
            WConio.cputs("                                               ")
            WConio.gotoxy(2,23)
            WConio.cputs("Enter command: ")
            cmd = raw_input()
            
	    if cmd == 'Test' or cmd == 'test' or cmd == 'TEST':
		f = open('C:\\PyBot\\cmd.txt', 'w')
		f.write('test')
		f.close()
		WConio.gotoxy(0,25)
		WConio.cputs("                                                        ")
		WConio.gotoxy(0,25)
		WConio.cputs("'Test' command accepted.")
	    elif cmd == 'exit' or cmd == 'Exit' or cmd == 'close' or cmd == 'Close' or cmd == 'Quit' or cmd == 'quit':
		f = open('C:\\PyBot\\cmd.txt', 'w')
		f.write('exit')
		f.close()
		WConio.gotoxy(0,25)
		WConio.cputs("                                                        ")
		WConio.gotoxy(0,25)
		WConio.cputs("Click the X button, this function isn't working.")
		WConio.gotoxy(79, 1)
		WConio.cputs("/")
		WConio.gotoxy(78, 2)
		WConio.cputs("/")
		WConio.gotoxy(77, 3)
		WConio.cputs("/")
		WConio.gotoxy(76, 4)
		WConio.cputs("/")
            else:
		WConio.gotoxy(0,25)
		WConio.cputs("                                                        ")
		WConio.gotoxy(0,25)
		WConio.cputs("Command not recognized.")
				
class ParseCommands ( threading.Thread ):

    #def Test ():
		
    def run ( self ):
    	WConio.textcolor(WConio.LIGHTBLUE)
	while 1:
            t = open('C:\\PyBot\\cmd.txt', 'r')
            cmd = t.read()
            t.close()
            if cmd == '':
            	time.sleep(3)
		continue
            else:
		#self.Test()
		if cmd == 'test':
                    l = open('C:\\PyBot\\update.txt', 'r')
                    str = l.read().split("\n")
                    for i in str:
			if i != '':
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((i, 8888))
                            s.send('test')
                            s.close()
		#else:
                    #if cmd == 'exit':
                        #time.sleep(3)
			#WConio.clrscr()
			#WConio.gotoxy(0,0)
			#raise SystemExit
			#os._exit()
			#sys.exit()
		time.sleep(3)
		
t = GetConnections()
t.start()		
tt = UpdateOnlines()
tt.start()		
ttt = GetCommands()
ttt.start()
tttt = ParseCommands()
tttt.start()
		
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = ''
#port = 8888
#s.bind((host, port))
#print 'Awaiting connections'
#s.listen(1)

#array of connections
#every so many seconds delete array and fill again
#to find only online connections

#thread 1
#while 1:
#    conn, addr = s.accept()
#    if not in array :
#        array[array.length()-1] = conn
        #write new entry of array to file
        #call function to reprint list
    
#print 'client is at', addr

#data = conn.recv(1000000)
#if data == "Connecting":
#    conn.send("Accepting")
   
#data = conn.recv(1000000)
#print 'system data: ', data
#conn.send("Connected")



#thread 2 --is waiting for you to ask to send a command
#once a command is sent read file into new array
#look through array for bot to send command to
#call thread 3  (send over bots and command)




#thread3
#send command to designated bot/s
