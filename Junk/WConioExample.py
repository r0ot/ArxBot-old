# Works with Microsoft Windows dos box
# Shows some use of WConio written by Chris Gonnerman

# Written by Priyend Somaroo
# Copyright (c) 2008 Vardaan Enterprises, www.vardaan.com

# Use and distribute freely.
# No liability for any use of this code will be accepted. Use is
# without any warranty whatsoever

# Requires the package WConio by Chris Gonnerman
# E-Mail : chris.gonnerman@newcenturycomputers.net
# Web : http://newcenturycomputers.net/projects/wconio.html

import WConio

old_setting = WConio.gettextinfo()[4] & 0x00FF
WConio.clrscr()
WConio.textcolor(WConio.LIGHTCYAN)
WConio.settitle("PyBot Control Center")
WConio.gotoxy(2,2)
WConio.cputs("Welcome to the PyBot Control Center\n\r")
WConio.gotoxy(0,4)
WConio.cputs("127.0.0.1\n\r")
WConio.cputs("192.168.1.1\n\r")
WConio.gotoxy(0,25)
WConio.cputs("Random Output...")
WConio.gotoxy(2,23)
WConio.cputs("Enter command: ")
WConio.getch()
WConio.gotoxy(0,25)