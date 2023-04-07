from Utils.Reader import Reader
from Packets.Messages.Server.Alliance.AllianceData  import AllianceData


class CreateAlliance(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        self.readString()  # AllianceName
        self.readString()  # AllianceDesc

        self.readInt()  # AllianceBadge

        self.readInt()  # AllianceType
        self.readInt()  # RequiredScore

    def process(self):
        AllianceData(self.device).Send()