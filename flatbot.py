# Test for a simple IRC bot in python
# Author: Max Blank
# Last changed: May 02 2016
# Feel free to use, contribute, expand and modify AT YOUR OWN RISK

import socket
import ssl
import time

#Settings
server = "port80a.se.quakenet.org"
port = 6667
channel = "#ossiostborn23"
botnick = "flatbot"
pingflag = 1
password = "testpass123"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "Connecting to %s:%d..." % (server, port)
#Establishing connection set nickname and join channel
irc.connect((server, port))
time.sleep(1)
#irc.send("PASS " + password)
#irc.send("USER flatbot . . :Testbot\n")
irc.send("NICK " + botnick + "\n")
#irc.send("PRIVMSG nickserv :iNOOP\r\n")
#irc.send("JOIN " + channel)

while pingflag:	#Answer ping message, register user, join channel
	text = irc.recv(2048)
	print text
	
	if text.find("PING") != -1:
		time.sleep(1)
		answer = "PONG " + text.split("PING :")[1] + "\n"
		print answer
		pingflag = 0
		irc.send(answer)
		#time.sleep(2)
		irc.send("USER flatbot . . :A simple Bot\n")
		time.sleep(4)
		#irc.send("JOIN " + channel + "\n")
#irc.send("JOIN " + channel + "\r\n")

while 1:
	text = irc.recv(2048)
	print text

	if text.find("PING ") != -1:
		answer = "PONG " + text.split("PING :")[1] + "\n"
		print answer
		irc.send(answer)
	
	if text.find("!hi ") != -1:
		irc.send("PRIVMSG " + channel + " Hello!\n")
	
	if text.find("!join") != -1:
		print "Trying to join channel " + channel + "\r\n"
		irc.send("JOIN " + channel + "\r\n")
