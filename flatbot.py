# Test for a simple IRC bot in python
# Author: Max Blank
# Last changed: May 02 2016
# Feel free to use, contribute, expand and modify AT YOUR OWN RISK

import socket
import ssl
import time

# Settings
server = b"port80a.se.quakenet.org"
port = 6667
channel = b"#ossiostborn23"
botnick = b"flatbot"
pingflag = 1
password = b"testpass123"
username = "user"
hostname = "host"
servername = "server"
realname = ":Bot"
identresponse = ("USER %s %s %s %s\r\n" % (username, hostname, servername, realname))

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to %s:%d..." % (server.decode('utf-8'), port))
# Establishing connection set nickname and join channel
irc.connect((server, port))
time.sleep(1)
# irc.send("PASS " + password)
# irc.send("USER flatbot . . :Testbot\n")
irc.send(b"NICK " + botnick + b"\r\n")
# irc.send("PRIVMSG nickserv :iNOOP\r\n")
# irc.send("JOIN " + channel)

while pingflag:  # Answer ping message, register user, join channel
    text = irc.recv(2048)
    print(text.decode('utf-8'))

    if text.find(b"PING") != -1:
        time.sleep(1)
        answer = b"PONG " + text.split(b"PING ")[1] + b"\r\n"
        print(answer.decode('utf-8'))
        pingflag = 0
        # irc.send(b"Antwort: " + answer)
        # time.sleep(2)
        # identresponse = ("USER %s %s %s %s\n" % (username, hostname, servername, realname))
        print("Send ident: " + identresponse)
        irc.send(identresponse.encode('utf-8'))
        time.sleep(4)

    if text.find(b"NOTICE AUTH :*** No ident response") != -1:
        time.sleep(1)
        print("Send ident response: " + identresponse)
        irc.send(identresponse.encode('utf-8'))
        irc.send(b"/NICK " + botnick + b"\r\n")
        pingflag = 0


while 1:
    text = irc.recv(2048)
    print(text.decode('utf-8'))

    # staying alive
    if text.find(b"PING ") != -1:
        answer = b"PONG " + text.split(b"PING ")[1] + b"\r\n"
        print(answer.decode('utf-8'))
        irc.send(answer)

    # greeting
    if text.find(b"!hi ") != -1:
        print("greet")
        print("Channel: " + channel.decode('utf-8'))
        answer = b"PRIVMSG " + channel + b" Hello!\r\n"
        print(answer.decode('utf-8'))
        irc.send(answer)

    # getting invited to a channel
    if text.find(b"!join") != -1:
        print("join")
        channel = text.split(b"!join ")[1].split(b"\r\n")[0]
        print(channel)
        print("Trying to join channel " + channel.decode('utf-8') + "\r\n")
        irc.send(b"JOIN " + channel + b"\r\n")

    #TODO: more functions :D
