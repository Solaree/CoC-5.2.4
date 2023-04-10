import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class AllianceKickOutStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 5

    def encode(self):

        self.writeString(config['AllianceKickOutMessage'])  # Message

        self.writeInt(config['AllianceHighID'])  # AllianceHighID
        self.writeInt(config['AllianceLowID'])  # AllianceLowID

        self.writeString(config['AllianceName'])  # AllianceName

        self.writeInt(config['AllianceBadge'])  # AllianceBadge