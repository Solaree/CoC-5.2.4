from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.Alliance.AllianceStreamEntryMessage import *


class ChatToAllianceStreamMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        self.readString()  # Message

    def process(self):
        AllianceStreamEntryMessage(self.client, self.player).Send()