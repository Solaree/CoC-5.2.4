import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class JoinAllianceResponseAvatarStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 3
    
    def encode(self):

        self.writeInt(config['AllianceHighID'])  # AllianceHighID
        self.writeInt(config['AllianceLowID'])  # AllianceLowID

        self.writeString(config['AllianceName'])  # AllianceName

        self.writeInt(config['AllianceBadge'])  # AllianceBadge

        self.writeString(config['AllianceMailMessage'])  # Message

        self.writeByte(1)

        self.writeInt(config['SenderHomeHighID'])  # SenderHomeHighID
        self.writeInt(config['SenderHomeLowID'])  # SenderHomeLowID