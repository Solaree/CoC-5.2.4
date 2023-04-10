from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.Avatar.AvatarProfileMessage import *


class AskForAvatarProfileMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device
    
    def decode(self):

        self.readInt()  #AvatarHighID
        self.readInt()  #AvatarLowID

        self.readInt()  # AllianceHighID
        self.readInt()  # AllianceLowID

        self.readByte()

        self.readInt()  # HomeHighID
        self.readInt()  # HomeLowID

    def process(self):
        AvatarProfileMessage(self.client, self.player).Send()