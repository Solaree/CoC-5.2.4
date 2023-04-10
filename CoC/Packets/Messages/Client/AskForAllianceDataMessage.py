from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.Alliance.AllianceDataMessage import *


class AskForAllianceDataMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        self.readInt()  # AllianceHighID
        self.readInt()  # AllianceLowID

    def process(self):
        AllianceDataMessage(self.client, self.player).Send()