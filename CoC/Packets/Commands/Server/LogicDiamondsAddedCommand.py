from Utils.Writer import Writer


class LogicDiamondsAddedCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = 7

    def encode(self):

        self.writeByte(1)  # GetFree

        self.writeInt(999)  # Amount

        self.writeString("G:0")  # TransactionId