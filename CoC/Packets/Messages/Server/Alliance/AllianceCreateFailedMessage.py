import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class AllianceCreateFailedMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24332

    def encode(self):

        self.writeInt(1)