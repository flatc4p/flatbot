"""
FU - very basic module for flatbot
Author: Max B.
Last changed: Mar 26 2020
Functionality: "!fu" command triggers a personalized insulting response
"""

class Fu(FlatModule):
    def __init__(self,name, command, debugmsg, *args, **kwargs):
        print(self, args, kwargs)


    def run(text):
        if text.find(command) != -1:
            print(debugmsg)
            channel = getChannel(text)
            recipient = getRecipient(text)
            irc.send(b"PRIVMSG " + channel + b" :Well, thank you! And a merry \"Fuck you\" to yoi too, " + recipient + b"!\r\n")

        if text.find(name + b" -help") != -1:
            print(debugmsg + " - usage")
            channel = getChannel(text)
            recipient = getRecipient(text)
            usage(channel)


    def usage(channel):
        irc.send(b"PRIVMSG " + channel + b" :Module " + name + " - Usage:\r\n")
        irc.send(b"PRIVMSG " + channel + b" :" + command + b" - " + usagemsg + b"\r\n")


