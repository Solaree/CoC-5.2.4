from Utils.Writer import Writer


class LogicChangeAllianceRoleCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = 8

    def encode(self):

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeInt(0)  # Role