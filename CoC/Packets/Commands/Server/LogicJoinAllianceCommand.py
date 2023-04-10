from Utils.Writer import Writer


class LogicJoinAllanceCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = 1

    def encode(self):

        self.writeInt()
        self.writeInt()

        self.writeString()

        self.writeInt()

        self.writeByte()
