from Utils.Reader import Reader
from Packets.Messages.Server.Alliance.DonateAllianceUnit import DonateAllianceUnit


class AskForAllianceUnitDonations(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        DonateAllianceUnit(self.device).Send()