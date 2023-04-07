from Utils.Reader import Reader
from Packets.Messages.Server.Alliance.Stream.AllianceStream import *


class AskForAllianceStream(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        AllianceStream(self.device).Send()