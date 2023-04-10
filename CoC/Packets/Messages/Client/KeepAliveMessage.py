from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.KeepAliveOkMessage import *


class KeepAliveMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self):
        KeepAliveOkMessage(self.device).Send()