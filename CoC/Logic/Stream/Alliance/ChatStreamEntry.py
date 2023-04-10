import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class ChatStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 2

    def encode(self):

        self.writeString(config['AllianceChatMessage'])  # Message