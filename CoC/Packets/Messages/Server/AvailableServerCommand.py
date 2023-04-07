from Utils.Writer import Writer
from Packets.Commands.Server.LogicChangeAvatarNameCommand import *
from Packets.Commands.Server.LogicChangeLeagueCommand import *


class AvailableServerCommand(Writer):

    def __init__(self, device, commandID):
        super().__init__(device)
        self.id = 24111
        self.device = device
        self.commandID = commandID

    def encode(self):

        commands = {
            3: LogicChangeAvatarNameCommand,
            535: LogicChangeLeagueCommand
        }

        if self.commandID in commands:

            self.writeInt(self.commandID)
            commands[self.commandID].encode(self)
        
        else:
            print(f"[SERVER] Cannot create command! ID: {self.commandID}")