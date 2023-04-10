from Utils.Writer import Writer


class AllianceEventStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 4

    def encode(self):

        self.writeInt(0)  # EventType

        self.writeInt(0)  # AvatarHighID
        self.writeInt(1)  # AvatarLowID

        self.writeString("Solar")  # AvatarName