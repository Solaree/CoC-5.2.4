from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.NpcDataMessage import *


class AttackNpcMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):

        self.readInt()

    def process(self):
        NpcDataMessage(self.client, self.player).Send()