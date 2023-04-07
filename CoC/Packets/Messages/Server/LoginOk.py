from Utils.Writer import Writer


class LoginOk(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):

        self.writeInt(0)  # AccountHighID
        self.writeInt(1)  # AccountLowID
        self.writeInt(0)  # HomeHighID
        self.writeInt(1)  # HomeLowID

        self.writeString("a77bad4dc5241ccb44d5a541376396208f92af8")  # PassToken
        self.writeString()  # FacebookID
        self.writeString()  # GameCenterID

        self.writeInt(0)  # MajorVersion
        self.writeInt(0)  # BuildVersion
        self.writeInt(0)  # ContentVersion

        self.writeString("dev")  # ServerEnvironment

        self.writeInt(0)  # PlayTimeSeconds
        self.writeInt(0)  # SessionCount
        self.writeInt(0)  # DaysSinceStartedPlaying

        self.writeString()  # FacebookAppId
        self.writeString()  # ServerTime
        self.writeString()  # AccountCreatedDate

        self.writeInt(0)  # StartupCooldownSeconds

        self.writeString()  # GoogleServiceId