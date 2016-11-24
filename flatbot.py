# Test for a simple IRC bot in python
# Author: Max Blank
# Last changed: Nov 24 2016
# Feel free to use, contribute, expand and modify AT YOUR OWN RISK

import socket
# import ssl
import time

# Settings
server = b"port80b.se.quakenet.org"
port = 6667
botnick = b"flatzbot"
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
            irc.send(b"/NICK " + botnick + b"\r\n")
            pingflag = 0


def loop():
    """Main loop parsing the chat and reacting to keywords"""
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
            channel = text.split(b"PRIVMSG ")[1]
            channel = channel.split(b" ")[0]
            recipient = text.split(b"!~")[0]
            recipient = recipient.split(b":")[1]


        #TODO: more functions :D

# Connect to irc server
connect(server, port, botnick, identresponse)
# Loop chatbot functionality
loop()
