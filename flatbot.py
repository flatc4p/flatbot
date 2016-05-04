# Test for a simple IRC bot in python
# Author: Max Blank
# Last changed: May 02 2016
# Feel free to use, contribute, expand and modify AT YOUR OWN RISK

import socket
import ssl

#Settings
server = "port80a.se.quakenet.org"
port = 6667
channel = "#ossiostborn23"
botnick = "flatbot"
pingflag = 1

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#irc = ssl.wrap_socket(irc_sock)

print "Connecting to %s:%d..." % (server, port)
#Establishing connection set nickname and join channel
irc.connect((server, port))
#irc.send("USER " + botnick + " " + botnick + " " + "RasPi :Testbot\n")
#irc.send("NICK " + botnick + "\n")
#irc.send("PRIVMSG nickserv :iNOOP\r\n")
while pingflag:
	text = irc.recv(50)
	if text.find("PING ") != -1:
		irc.send("PONG " + text.split() [1] + "\r\n")
		print "PONG " + text.split() [1] + "\r\n"
		pingflag = 0
#irc.send("JOIN " + channel)

while 1:
	text = irc.recv(2048)
	print text
	
	if text.find("PING") != -1:
		irc.send("PONG " + text.split() [1] + "\r\n")
