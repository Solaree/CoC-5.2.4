from Utils.Reader import Reader
from Logic.Player import Player
# from Packets.Messages.Server.AvailableServerCommand import AvailableServerCommand


class LogicBuyBuildingCommand(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        
        self.X = self.readInt()
        self.Y = self.readInt()  

        self.buildingID = self.readInt()

    def process(self):
        pass
        #if self.buildingID == 1000022:
            #AvailableServerCommand(self.client, self.player, 28000000, self.buildingID, self.X, self.Y).Send()  # BarbarianKing

        #if self.buildingID == 1000025:
            #AvailableServerCommand(self.client, self.player, 28000001, self.buildingID, self.X, self.Y).Send()  # ArcherQueen