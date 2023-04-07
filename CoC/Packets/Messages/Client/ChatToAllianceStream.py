from Utils.Reader import Reader
from Packets.Messages.Server.Alliance.Stream.AllianceStream import AllianceStream


class ChatToAllianceStream(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        self.msg = self.readString()  # Message

    def process(self):

        AllianceStream(self.device, self.msg).sendByID(1)