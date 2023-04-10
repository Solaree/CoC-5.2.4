from Utils.Writer import Writer
from Logic.AllianceFullEntry import AllianceFullEntry

class AllianceDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24301

    def encode(self):
        AllianceFullEntry.encode(self)