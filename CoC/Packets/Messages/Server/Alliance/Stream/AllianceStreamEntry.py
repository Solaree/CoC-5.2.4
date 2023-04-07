from Utils.Writer import Writer


class AllianceStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24312

    def encode(self):

        self.writeInt(1)