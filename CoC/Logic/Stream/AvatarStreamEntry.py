import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class AvatarStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 6
    
    def encode(self):

        self.writeInt(config['AccountHighID'])  # HighID
        self.writeInt(config['AccountLowID'])  # LowID

        self.writeInt(config['SenderHomeHighID'])  # SenderAvatarHighID
        self.writeInt(config['SenderHomeLowID'])  # SenderAvatarLowID

        self.writeString(config['Name'])  # Name

        self.writeInt(config['SenderLevel'])  # SenderLevel
        self.writeInt(config['SenderLeagueType'])  # SenderLeagueType
        self.writeInt(config['SenderMessageAgeSeconds'])  # AgeSeconds

        self.writeByte(0)  # IsRemoved
        self.writeByte(1)  # IsNew