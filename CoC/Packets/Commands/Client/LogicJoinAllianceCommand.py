from Utils.Reader import Reader
from Packets.Messages.Server.AvailableServerCommand import *


class LogicJoinAllanceCommand(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):

        self.readInt()
        self.readInt()

        self.readString()

        self.readInt()

        self.readByte()
    
    def process(self):
        pass
