from Utils.Writer import Writer


class DeviceLinkedStreamEntry(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.StreamEntryType = 9
    
    def encode(self):
        pass