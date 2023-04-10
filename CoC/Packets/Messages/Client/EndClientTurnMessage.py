from Utils.Reader import Reader
from Logic.Player import Player
from Packets.CommandFactory import commands
from Packets.Messages.Server.AvailableServerCommandMessage import *


class EndClientTurnMessage(Reader):

    def __init__(self, data, device, commandsID):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device
        self.commandsID = commandsID

    def decode(self):

        self.tick = self.readInt()  # SubTick

        self.readInt()  # Checksum

        self.commandID = self.readInt()  # CommandsCount

    def process(self):
        command = commands[self.commandsID]
        command.decode(self)
        command.process(self)
        command(self.client, self.player).Send() # Exception for OutOfSyncMessage

        AvailableServerCommandMessage(self.client, self.player).Send()