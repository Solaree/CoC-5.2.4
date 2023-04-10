from Utils.Writer import Writer
from Logic.Stream.Alliance.AllianceEventStreamEntry import *
from Logic.Stream.Alliance.ChatStreamEntry import *
from Logic.Stream.Alliance.JoinRequestAllianceStreamEntry import *
from Logic.Stream.Alliance.ReplayStreamEntry import *

class AllianceStreamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24311

    def encode(self):

        self.writeInt()  # AllianceStreamCount

        ChatStreamEntry.encode(self)
        JoinRequestAllianceStreamEntry.encode(self)
        AllianceEventStreamEntry.encode(self)
        ReplayStreamEntry.encode(self)