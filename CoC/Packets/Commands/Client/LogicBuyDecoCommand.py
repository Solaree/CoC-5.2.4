from Utils.Reader import Reader
from Logic.Player import Player
# from Packets.Messages.Server.AvailableServerCommand import AvailableServerCommand


class LogicBuyDecoCommand(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        
        self.X = self.readInt()
        self.Y = self.readInt()  

        self.decoID = self.readInt()

    def process(self):
        pass