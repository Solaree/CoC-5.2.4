import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class JoinRequestAllianceStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 3

    def encode(self):

        self.writeString(config['AllianceJoinRequestMessage'])  # Message
        self.writeString(config['Name'])  # ResponderName

        self.writeInt(0)  # State