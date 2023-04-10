from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.Alliance.DonateAllianceUnitMessage import *


class AskForAllianceUnitDonationsMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self):
        DonateAllianceUnitMessage(self.client, self.player).Send()