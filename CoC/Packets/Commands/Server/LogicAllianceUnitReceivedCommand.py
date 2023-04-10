from Utils.Writer import Writer


class LogicAllianceUnitReceivedCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = 5

    def encode(self):

        self.writeString()

        self.writeInt(1)

        self.writeInt(0)
