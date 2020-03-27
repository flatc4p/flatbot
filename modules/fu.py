"""
FU - very basic module for flatbot
Author: Max B.
Last changed: Mar 26 2020
Functionality: "!fu" command triggers a personalized insulting response
"""
from modules import flatmodule

class Fu(flatmodule.FlatModule):

    def run(self, text):
        if text.find(self.command) != -1:
            print(self.debugmsg)
            channel = self.getChannel(text)
            recipient = self.getRecipient(text)
            self.irc.send(b"PRIVMSG " + channel + b" :Well, thank you! And a merry \"Fuck you\" to you too, " + recipient + b"!\r\n")

        if text.find(self.name + b" -help") != -1:
            print(self.debugmsg + " - usage")
            channel = self.getChannel(text)
            recipient = self.getRecipient(text)
            self.usage(channel)

    def usage(self, channel):
        self.irc.send(b"PRIVMSG " + channel + b" :Module " + self.name + " - Usage:\r\n")
        self.irc.send(b"PRIVMSG " + channel + b" :" + self.command + b" - " + self.usagemsg + b"\r\n")
        