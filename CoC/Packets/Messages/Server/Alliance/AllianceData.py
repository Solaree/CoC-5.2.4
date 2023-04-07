from Utils.Writer import Writer


class AllianceData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24301

    def encode(self):

        # AllianceHeaderEntry

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString("SolarLand")  # AllianceName
    
        self.writeInt(13000001)  # AllianceBadge

        self.writeInt(1)  # AllianceType
        self.writeInt(1)  # NumberOfMembers
        self.writeInt(0)  # Score
        self.writeInt(1)  # RequiredScore

        self.writeString()  # AllianceDescription


        # AllianceFullEntry

        self.writeString(None)  # AllianceDescription
        
        self.writeInt()  # AllianceMembers


        # AllianceMemberEntry

        self.writeInt(0)  # AvatarHighID
        self.writeInt(1)  # AvatarLowID

        self.writeString(None)  # FacebookID
        self.writeString("Solar")  # Name

        self.writeInt(0)  # Role
        self.writeInt(99)  # ExpLevel
        self.writeInt(1)  # LeagueType
        self.writeInt(999)  # Score
        self.writeInt(999)  # Donations
        self.writeInt(999)  # DonationsReceived
        self.writeInt(0)  # Order
        self.writeInt(0)  # PreviousOrder

        self.writeByte(1)  # IsNewMember

        self.writeInt(0)  # HomeHighID
        self.writeInt(1)  # HomeHighID