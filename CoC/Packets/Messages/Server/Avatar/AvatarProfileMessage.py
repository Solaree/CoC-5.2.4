import json
from Utils.Writer import Writer
from Logic.ClientAvatar import LogicClientAvatar

config = json.load(open("config.json", "r"))


class AvatarProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24334
    
    def  encode(self):

        LogicClientAvatar.encode(self)

        self.writeInt(config['Donations'])  # Donations
        self.writeInt(config['DonationsReceived'])  # DonationsReceived