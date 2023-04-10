from Utils.Writer import Writer
from Logic.Stream.Alliance.AllianceEventStreamEntry import *
from Logic.Stream.Alliance.ChatStreamEntry import *
from Logic.Stream.Alliance.JoinRequestAllianceStreamEntry import *
from Logic.Stream.Alliance.ReplayStreamEntry import *


class AllianceJoinOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24303

    def encode(self):
        pass
