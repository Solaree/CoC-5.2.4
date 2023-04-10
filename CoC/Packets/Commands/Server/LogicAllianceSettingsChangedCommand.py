from Utils.Writer import Writer


class LogicAllianceSettingsChangedCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = 6

    def encode(self):

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        self.writeInt(0)