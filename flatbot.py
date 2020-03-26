# Test for a simple IRC bot in python
# Author: Max Blank
# Last changed: Mar 26 2020
# Feel free to use, contribute, expand and modify AT YOUR OWN RISK

import socket
# import ssl
import time
import random

# Settings
server = b"port80b.se.quakenet.org"
port = 6667
channel = b"#ossiostborn23"
botnick = b"flatdevbot"
pingflag = 1
password = b"testpass123"
username = "user"
hostname = "host"
servername = "server"
realname = ":Bot"
identresponse = ("USER %s %s %s %s\r\n" % (username, hostname, servername, realname))
quitmessages = (b"Cya!", b"Habe d'Ehre!", b"Adios, amigos!", b"Pfiad Eich!", b"Macht's gut, ihr Trottel!")

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to %s:%d..." % (server.decode('utf-8'), port))
# Establishing connection set nickname and join channel
irc.connect((server, port))
time.sleep(1)
irc.send(b"NICK " + botnick + b"\r\n")

while pingflag:  # Answer ping message, register user, join channel
    text = irc.recv(2048)
    print(text.decode('utf-8'))

    if text.find(b"PING") != -1:
        answer = b"PONG " + text.split(b"PING ")[1] + b"\r\n"
        print(answer.decode('utf-8'))

    if text.find(b"NOTICE AUTH :*** Checking Ident") != -1:
        time.sleep(1)
        print("Send ident response: " + identresponse)
        irc.send(identresponse.encode('utf-8'))
        #irc.send(b"/NICK " + botnick + b"\r\n")
        pingflag = 0


while 1:
    text = irc.recv(2048)
    print(text.decode('utf-8'))

    # staying alive
    if text.find(b"PING ") != -1:
        answer = b"PONG " + text.split(b"PING ")[1] + b"\r\n"
        print(answer.decode('utf-8'))
        irc.send(answer)

    # greeting back
    if text.find(b"!hi") != -1:
        print("greet")
        recipient = text.split(b"!hi")
        print("Channel: " + channel.decode('utf-8'))
        answer = b"PRIVMSG " + channel + b" :Hello!\r\n"
        print(answer.decode('utf-8'))
        irc.send(answer)


    # getting invited to a channel
    if text.find(b"!join") != -1:
        print("join")
        channel = text.split(b"!join ")[1].split(b"\r\n")[0]
        print(channel)
        print("Trying to join channel " + channel.decode('utf-8') + "\r\n")
        irc.send(b"JOIN " + channel + b"\r\n")

    # get insulted by dolph
    if text.find(b"!fu") != -1:
        print("insult")
        channel = text.split(b"PRIVMSG ")[1]
        channel = channel.split(b" ")[0]
        recipient = text.split(b"!~")[0]
        recipient = recipient.split(b":")[1]
        print(recipient)
        irc.send(b"PRIVMSG " + channel + b" :Well, thank you! And a merry \"Fuck you\" to you too, " \
                 + recipient + b"!\r\n")

    # greeting a new visitor
    if text.find(b"JOIN") != -1:
        print("greet")

	# change nick at runtime
    if text.find(b"!nick") != -1:
        print("nick change")
        botnick = text.split(b"!nick ")[1]
        botnick = botnick.split(b"\r\n")[0]
        irc.send(b"NICK " + botnick + b"\r\n")

    if text.find(b"!quit") != -1:
        print("quitting")
        irc.send(b"QUIT :" + random.choice(quitmessages) + b"\r\n")
        break

    #TODO: more functions :D
