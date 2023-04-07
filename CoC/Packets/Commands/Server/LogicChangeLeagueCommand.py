from Utils.Writer import Writer

class LogicChangeLeagueCommand(Writer):

    def encode(self):
        
        self.writeByte(1)

        self.writeInt(0)  # LeagueHighID
        self.writeInt(1)  # LeagueLowID

        self.writeInt()  # LeagueType