from Utils.Writer import Writer
from Logic.Stream.Avatar.JoinAllianceResponseAvatarStreamEntry import *
from Logic.Stream.Avatar.AllianceInvationAvatarStreamEntry import *
from Logic.Stream.Avatar.AllianceKickOutStreamEntry import *
from Logic.Stream.Avatar.AllianceMailAvatarStreamEntry import *
from Logic.Stream.Avatar.BattleReportStreamEntry import *
from Logic.Stream.Avatar.DeviceLinkedStreamEntry import *

class AvatarStreamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24411
    
    def encode(self):
        self.writeInt(6)  # StreamEntryCount
        self.writeInt(1)  # StreamEntryType

        JoinAllianceResponseAvatarStreamEntry.encode(self)
        AllianceInvationAvatarStreamEntry.encode(self)
        AllianceKickOutStreamEntry.encode(self)
        AllianceMailAvatarStreamEntry.encode(self)
        BattleReportStreamEntry.encode(self)
        DeviceLinkedStreamEntry.encode(self)