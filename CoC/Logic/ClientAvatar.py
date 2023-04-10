import json
from Utils.Writer import Writer

config = json.load(open("config.json", "r"))


class LogicClientAvatar(Writer):

    def encode(self):

        self.writeInt(0)

        self.writeInt(config['AccountHighID'])  # DefaultHighID
        self.writeInt(config['AccountLowID'])  # DefaultLowID
        self.writeInt(config['HomeHighID'])  # CurrentHomeHighID
        self.writeInt(config['HomeLowID'])  # CurrentHomeLowID

        self.writeByte(1)  # IsInAlliance

        self.writeInt(config['AllianceHighID'])  # AllianceHighID
        self.writeInt(config['AllianceLowID'])  # AllianceLowID

        self.writeString(config['AllianceName'])  # AllianceName

        self.writeInt(config['AllianceBadge'])  # AllianceBadge
        self.writeInt(config['AllianceRole'])  # AllianceRole

        self.writeByte(1)

        self.writeInt(config['LeagueInstanceHighID'])  # LeagueInstanceHighID
        self.writeInt(config['LeagueInstanceLowID'])  # LeagueInstanceLowID

        self.writeByte(1)

        self.writeInt(config['LastLeagueInstanceHighID'])  # LastLeagueInstanceHighID
        self.writeInt(config['LastLeagueInstanceLowID'])  # LastLeagueInstanceLowID
        self.writeInt(config['LeagueType'])  # LeagueType

        self.writeInt(0)
        self.writeInt(10)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString(config['Name'])  # Name
        self.writeString(None)  # FacebookID

        self.writeInt(config['ExpLevel'])   # ExpLevel
        self.writeInt(config['ExpPoints'])  # ExpPoints
        self.writeInt(config['Diamonds'])  # Diamonds
        self.writeInt(0)  # FreeDiamonds
        self.writeInt(0)  # AttackRating
        self.writeInt(0)  # AttackKFactor
        self.writeInt(config['Score'])  # Score
        self.writeInt(config['AttackWinCount'])  # AttackWinCount
        self.writeInt(config['AttackLoseCount'])  # AttackLoseCount
        self.writeInt(config['DefenseWinCount'])  # DefenseWinCount
        self.writeInt(config['DefenseLoseCount'])  # DefenseLoseCount
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeByte(0)  # NameSetByUser

        self.writeByte(0)

        self.writeInt(0) # CumulativePurchasedDiamonds

        ##### ARAYS #####

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