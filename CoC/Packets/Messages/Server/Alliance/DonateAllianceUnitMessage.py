from Utils.Writer import Writer


class DonateAllianceUnitMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 14310

    def encode(self):

        self.writeInt(10000000)  # AllianceUnitCharacter

        self.writeInt(0)  # StreamHighID
        self.writeInt(1)  # StreamLowID
