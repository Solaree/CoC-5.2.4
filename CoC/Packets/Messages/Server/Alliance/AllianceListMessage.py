from Utils.Writer import Writer


class AllianceListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24310

    def encode(self):

        self.writeString()

        self.writeInt(1)  # Amount of clubs in the club list