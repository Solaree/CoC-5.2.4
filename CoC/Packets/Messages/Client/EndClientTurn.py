from Utils.Reader import Reader
from Packets.CommandFactory import commands

class EndClientTurn(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):

        self.tick = self.readInt()  # Tick

        self.readInt()  # Checksum

        if self.tick != 0:
            self.commandID = self.readInt()  # CommandsCount

    def process(self):

        if self.tick != 0:
            if self.commandID in commands:
                command = commands[self.commandsID]

                try:
                    command.decode(self)
                    command.process(self)

                except AttributeError:
                    command(self.device).send() # Exception for OutOfSyncMessage

            else:
                print(f'[CLIENT] Unhandled Command! ID: {self.commandID}')