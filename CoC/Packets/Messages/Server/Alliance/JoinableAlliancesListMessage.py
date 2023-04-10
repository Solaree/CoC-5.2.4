from Utils.Writer import Writer


class JoinableAlliancesListMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24304

    def encode(self):

        self.writeInt(0)
        self.writeInt(1)
