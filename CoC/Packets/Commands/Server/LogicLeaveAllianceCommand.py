from Utils.Writer import Writer


class LogicLeaveAllanceCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = 2

    def encode(self):

        self.writeInt()  # HighID
        self.writeInt()  # LowID