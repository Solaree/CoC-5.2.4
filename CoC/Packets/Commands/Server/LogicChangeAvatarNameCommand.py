from Utils.Writer import Writer


class LogicChangeAvatarNameCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = 3

    def encode(self):

        self.writeString("Solar")