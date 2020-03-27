"""
This module acts as a base module for future flatbot modules
Following variables must be present for each module:
    - name:     specifying how the module is called
    - command:  should start with "!", triggers the module to execute "run()"
    - debugmsg: short message thats printed in the log, when a command is recognized
    - usagemsg: short usage string that is posted, if a command is invoked with an additional "- help"
The function "run()" contains the code that's executed, when "command" is recognized in a channel that's inhabited by the bot.
The base class provides the functions "getChannel()" and "getRecipient()" that get passed a string. If the string contains a "PRIVMSG" the originating channel and sender will be extracted by "getChannel()" or "getRecipient()" respectively.

Author: Max. B.
Last changed: Mar 27 2020
Disclaimer: use at your own risk only!
"""

class FlatModule:

    def __init__(self, irc, name, command, debugmsg, usagemsg, *args, **kwargs):
        print(b"Module " + name + " loaded!")
        self.irc        = irc
        self.name       = name
        self.debugmsg   = debugmsg
        self.command    = command
        self.usagemsg   = usagemsg

    def run(self, text):
        print(self.debugmsg)

    def usage(self, channel):
        print(self.usagemsg)

    def getChannel(self, text):
        channel = text.split(b"PRIVMSG ")[1]
        channel = channel.split(b" ")[0]
        return channel

    def getRecipient(self, text):
        recipient = text.split(b"!~")[0]
        recipient = recipient.split(b":")[1]
        return recipient
