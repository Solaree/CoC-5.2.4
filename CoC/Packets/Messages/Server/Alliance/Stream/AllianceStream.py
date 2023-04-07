from Utils.Writer import Writer


class AllianceStream(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24311

    def encode(self):

        self.writeInt(1)
        self.writeInt(1)
        self.writeInt(1)