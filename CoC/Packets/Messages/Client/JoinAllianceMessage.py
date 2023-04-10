from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.Alliance.AllianceStreamMessage import *
from Packets.Messages.Server.Alliance.AllianceStreamEntryMessage import *


class JoinAllianceMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        
        self.readInt()  # HighID
        self.readInt()  # LowID
    
    def process(self):
        AllianceStreamMessage(self.client, self.player).Send()
        AllianceStreamEntryMessage(self.client, self.player).Send()