from Utils.Writer import Writer

class LogicClientAvatar(Writer):

    def encode(self):

        self.writeInt(0)  # DefaultHighID
        self.writeInt(0)  # DefaultLowID
        self.writeInt(0)  # CurrentHomeHighID
        self.writeInt(1)  # CurrentHomeLowID

        self.writeByte(1)  # IsInAlliance

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString("SolarLand")  # AllianceName

        self.writeInt(13000001)  # AllianceBadge
        self.writeInt(1)  # AllianceRole

        self.writeByte(1)

        self.writeInt(0)  # LeagueInstanceHighID
        self.writeInt(1)  # LeagueInstanceLowID

        self.writeByte(1)

        self.writeInt(0)  # LastLeagueInstanceHighID
        self.writeInt(1)  # LastLeagueInstanceLowID

        self.writeInt(10)  # LeagueType

        self.writeInt(0)
        self.writeInt(1)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString("Solar")  # Name
        self.writeString(None)  # FacebookID

        self.writeInt(99)   # ExpLevel
        self.writeInt(1000)  # ExpPoints
        self.writeInt(999)  # Diamonds
        self.writeInt(999)  # FreeDiamonds
        self.writeInt(1)  # AttackRating
        self.writeInt(1)  # AttackKFactor
        self.writeInt(999)  # Score
        self.writeInt(1337)  # AttackWinCount
        self.writeInt(0)  # AttackLoseCount
        self.writeInt(1337)  # DefenseWinCount
        self.writeInt(0)  # DefenseLoseCount

        self.writeByte(0)  # NameSetByUser

        self.writeInt(0) # CumulativePurchasedDiamonds

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeInt(0)

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)