from Utils.Reader import Reader
from Packets.Messages.Server.Alliance.AllianceList import AllianceList


class AskForJoinableAlliancesList(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        AllianceList(self.device).Send()