from Utils.Reader import Reader
from Packets.Messages.Server.AvailableServerCommand import *


class LogicLeaveAllanceCommand(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):

        self.readInt()  # HighID
        self.readInt()  # LowID

    def process(self):
        pass