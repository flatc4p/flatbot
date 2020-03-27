"""
Test for a simple IRC bot in python
Modular approach
flatbot.py - providing basic functionality (connect to irc server, set nickname, get invited to channel and greet new users)
TODO: add support to load modules during runtime
Author: Max Blank
Last changed: Mar 26 2020
Feel free to use, contribute, expand and modify AT YOUR OWN RISK
"""

import socket
import importlib
import time

# Settings
server = b"port80b.se.quakenet.org"
port = 6667
botnick = b"flatbot"
username = "user"
hostname = "host"
servername = "server"
realname = ":Bot"
identresponse = ("USER %s %s %s %s\r\n" % (username, hostname, servername, realname))

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect(server, port, botnick, identresponse):
    """Connect to an irc server"""
    print("Connecting to %s:%d..." % (server.decode('utf-8'), port))
    # Establishing connection set nickname and join channel
    irc.connect((server, port))
    time.sleep(1)
    irc.send(b"NICK " + botnick + b"\r\n")
    pingflag = 1

    while pingflag:  # Answer ping message, register user 
        text = irc.recv(2048)
        print(text.decode('iso-8859-1'))

        if text.find(b"PING") != -1:
            answer = b"PONG " + text.split(b"PING ")[1] + b"\r\n"
            print(answer.decode('utf-8'))

        if text.find(b"NOTICE AUTH :*** Checking Ident") != -1:
            time.sleep(1)
            print("Send ident response: " + identresponse)
            irc.send(identresponse.encode('utf-8'))
            irc.send(b"/NICK " + botnick + b"\r\n")
            pingflag = 0


def loop():
    """Main loop parsing the chat and reacting to keywords"""
    while 1:
        text = irc.recv(2048)
        print(text.decode('iso-8859-1'))

        # staying alive
        if text.find(b"PING ") != -1:
            answer = b"PONG " + text.split(b"PING ")[1] + b"\r\n"
            print(answer.decode('utf-8'))
            irc.send(answer)

        # greeting back
        if text.find(b"!hi") != -1:
            print("greet")
            recipient = text.split(b"!hi")
            channel = text.split(b"PRIVMSG ")[1]
            channel = channel.split(b" ")[0]
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

        # greeting a new visitor
        if text.find(b"JOIN") != -1:
            print("greet")
            channel = text.split(b"JOIN ")[1]
            channel = channel.split(b" ")[0].split(b"\r\n")[0]
            print(b"Channel: " + channel)
            recipient = text.split(b"!")[0]
            recipient = recipient.split(b":")[1]
            print(b"recipient: " + recipient)
            if(recipient == botnick):
                print("PRIVMSG " +channel.decode('utf-8') + " :Hi there. I'm a bot\r\n")
                irc.send(b"PRIVMSG " + channel + b" :Hi there. I'm a bot!\r\n")
            else:
                print("PRIVMSG " + channel.decode('utf-8') + " :Welcome, " + recipient.decode('utf-8') \
                      + "! Enjoy your stay!\r\n")
                irc.send(b"PRIVMSG " + channel + b" :Welcome, " + recipient + b"! Enjoy your stay!\r\n")
                
        #TODO: implement real modular approach enabling loading seperate modules at runtime

# Connect to irc server
connect(server, port, botnick, identresponse)
# Loop chatbot functionality
loop()
