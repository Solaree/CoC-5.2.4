from Utils.Writer import Writer
from Packets.Commands.Server.LogicJoinAllianceCommand import *
from Packets.Commands.Server.LogicLeaveAllianceCommand import *
from Packets.Commands.Server.LogicChangeAvatarNameCommand import *
from Packets.Commands.Server.LogicAllianceUnitReceivedCommand import *
from Packets.Commands.Server.LogicAllianceSettingsChangedCommand import *
from Packets.Commands.Server.LogicDiamondsAddedCommand import *
from Packets.Commands.Server.LogicChangeAllianceRoleCommand import *


class AvailableServerCommandMessage(Writer):

    def __init__(self, client, player, commandID):
        super().__init__(client)
        self.player = player
        self.device = client
        self.commandID = commandID
        self.id = 24111

    def encode(self):

        commands = {

            1: LogicJoinAllanceCommand,
            2: LogicLeaveAllanceCommand,
            3: LogicChangeAvatarNameCommand,
            5: LogicAllianceUnitReceivedCommand,
            6: LogicAllianceSettingsChangedCommand,
            7: LogicDiamondsAddedCommand,
            8: LogicChangeAllianceRoleCommand

        }

        if self.commandID in commands:
            self.writeInt(self.commandID)
            commands[self.commandID].encode(self)
        
        else:
            print(f"[SERVER] Cannot create command! ID: {self.commandID}")
