import json
from Utils.Writer import Writer

cache = str(json.load(open("JSON/OwnHomeData.json")))


class LogicClientHome(Writer):

    def encode(self):
        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        self.writeString(cache)  # HomeJSON

        self.writeInt(9999)  # ShieldDurationSeconds
        self.writeInt(1)  # DefenseRating
        self.writeInt(1)  # DefenseKFactor