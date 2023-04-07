from Utils.Reader import Reader
from Packets.Messages.Server.KeepAliveOk import *

class KeepAlive(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        KeepAliveOk(self.device).Send()