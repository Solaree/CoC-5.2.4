from Utils.Writer import Writer


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.device = client
        self.id = 24101

    def encode(self):

        # LogicClientHome

        self.writeInt(0)  # SecondsSinceLastSave
        self.writeInt(0)

        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID

        self.writeString("{\"buildings\":[{\"data\":1000001,\"lvl\":5,\"x\":20,\"y\":20},{\"data\":1000004,\"lvl\":9,\"x\":12,\"y\":29,\"res_time\":143996},{\"data\":1000000,\"lvl\":5,\"x\":29,\"y\":14,\"units\":[],\"storage_type\":0},{\"data\":1000015,\"lvl\":0,\"x\":10,\"y\":26},{\"data\":1000014,\"lvl\":2,\"x\":28,\"y\":21},{\"data\":1000004,\"lvl\":9,\"x\":23,\"y\":32,\"res_time\":143996},{\"data\":1000002,\"lvl\":9,\"x\":17,\"y\":12,\"res_time\":143996},{\"data\":1000002,\"lvl\":9,\"x\":18,\"y\":9,\"res_time\":143996},{\"data\":1000015,\"lvl\":0,\"x\":31,\"y\":25},{\"data\":1000003,\"lvl\":9,\"x\":12,\"y\":26},{\"data\":1000005,\"lvl\":9,\"x\":16,\"y\":28},{\"data\":1000006,\"lvl\":7,\"x\":9,\"y\":30,\"unit_prod\":{\"unit_type\":0}},{\"data\":1000008,\"lvl\":6,\"x\":24,\"y\":25},{\"data\":1000008,\"lvl\":6,\"x\":13,\"y\":20},{\"data\":1000002,\"lvl\":9,\"x\":25,\"y\":10,\"res_time\":143996},{\"data\":1000004,\"lvl\":9,\"x\":11,\"y\":13,\"res_time\":143996},{\"data\":1000006,\"lvl\":7,\"x\":14,\"y\":12,\"unit_prod\":{\"unit_type\":0}},{\"data\":1000009,\"lvl\":6,\"x\":17,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":30,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":26},{\"data\":1000002,\"lvl\":9,\"x\":10,\"y\":16,\"res_time\":143996},{\"data\":1000004,\"lvl\":9,\"x\":9,\"y\":19,\"res_time\":143996},{\"data\":1000005,\"lvl\":9,\"x\":13,\"y\":16},{\"data\":1000003,\"lvl\":9,\"x\":25,\"y\":13},{\"data\":1000000,\"lvl\":5,\"x\":18,\"y\":32,\"units\":[],\"storage_type\":0},{\"data\":1000013,\"lvl\":3,\"x\":24,\"y\":21},{\"data\":1000007,\"lvl\":3,\"x\":21,\"y\":8},{\"data\":1000002,\"lvl\":9,\"x\":9,\"y\":22,\"res_time\":143996},{\"data\":1000004,\"lvl\":9,\"x\":28,\"y\":11,\"res_time\":143996},{\"data\":1000009,\"lvl\":6,\"x\":25,\"y\":17},{\"data\":1000012,\"lvl\":3,\"x\":21,\"y\":17},{\"data\":1000006,\"lvl\":7,\"x\":24,\"y\":29,\"unit_prod\":{\"unit_type\":0}},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":13,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":21},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":20},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":19},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":25,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":26,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":30,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":23},{\"data\":1000010,\"lvl\":5,\"x\":31,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":27,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":27},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":26},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":25},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":18},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":17},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":16},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":12,\"y\":22},{\"data\":1000010,\"lvl\":5,\"x\":14,\"y\":23},{\"data\":1000002,\"lvl\":9,\"x\":15,\"y\":32,\"res_time\":143996},{\"data\":1000004,\"lvl\":9,\"x\":28,\"y\":29,\"res_time\":143996},{\"data\":1000008,\"lvl\":6,\"x\":16,\"y\":24},{\"data\":1000013,\"lvl\":3,\"x\":17,\"y\":20},{\"data\":1000000,\"lvl\":5,\"x\":32,\"y\":19,\"units\":[],\"storage_type\":0},{\"data\":1000009,\"lvl\":6,\"x\":20,\"y\":28},{\"data\":1000011,\"lvl\":2,\"x\":20,\"y\":24},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":19,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":20,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":21,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":22,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":23,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":12},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":13},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":14},{\"data\":1000010,\"lvl\":5,\"x\":24,\"y\":15},{\"data\":1000010,\"lvl\":5,\"x\":18,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":17,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":16,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":31},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":30},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":29},{\"data\":1000010,\"lvl\":5,\"x\":15,\"y\":28},{\"data\":1000011,\"lvl\":2,\"x\":21,\"y\":13},{\"data\":1000020,\"lvl\":1,\"x\":28,\"y\":25,\"units\":[],\"storage_type\":1,\"unit_prod\":{\"unit_type\":1}},{\"data\":1000010,\"lvl\":5,\"x\":29,\"y\":28},{\"data\":1000010,\"lvl\":5,\"x\":28,\"y\":28}],\"obstacles\":[{\"data\":8000008,\"x\":6,\"y\":6,\"loot_multiply_ver\":1},{\"data\":8000005,\"x\":37,\"y\":5,\"loot_multiply_ver\":1},{\"data\":8000007,\"x\":6,\"y\":4,\"loot_multiply_ver\":1},{\"data\":8000008,\"x\":35,\"y\":7,\"loot_multiply_ver\":1},{\"data\":8000005,\"x\":5,\"y\":29,\"loot_multiply_ver\":1},{\"data\":8000002,\"x\":4,\"y\":38,\"loot_multiply_ver\":1},{\"data\":8000008,\"x\":5,\"y\":36,\"loot_multiply_ver\":1},{\"data\":8000001,\"x\":7,\"y\":35,\"loot_multiply_ver\":1},{\"data\":8000007,\"x\":4,\"y\":9,\"loot_multiply_ver\":1},{\"data\":8000003,\"x\":29,\"y\":37,\"loot_multiply_ver\":1},{\"data\":8000001,\"x\":33,\"y\":4,\"loot_multiply_ver\":1},{\"data\":8000010,\"x\":26,\"y\":38,\"loot_multiply_ver\":1},{\"data\":8000013,\"x\":34,\"y\":33,\"loot_multiply_ver\":1},{\"data\":8000007,\"x\":32,\"y\":38,\"loot_multiply_ver\":1},{\"data\":8000000,\"x\":12,\"y\":8,\"loot_multiply_ver\":1},{\"data\":8000005,\"x\":4,\"y\":20,\"loot_multiply_ver\":1},{\"data\":8000005,\"x\":32,\"y\":10,\"loot_multiply_ver\":1},{\"data\":8000000,\"x\":38,\"y\":13,\"loot_multiply_ver\":1},{\"data\":8000013,\"x\":1,\"y\":34,\"loot_multiply_ver\":1},{\"data\":8000006,\"x\":1,\"y\":19,\"loot_multiply_ver\":1},{\"data\":8000000,\"x\":40,\"y\":29,\"loot_multiply_ver\":1}],\"traps\":[{\"data\":12000000,\"lvl\":2,\"x\":14,\"y\":15},{\"data\":12000000,\"lvl\":2,\"x\":27,\"y\":29},{\"data\":12000001,\"lvl\":0,\"x\":32,\"y\":24},{\"data\":12000001,\"lvl\":0,\"x\":28,\"y\":15},{\"data\":12000000,\"lvl\":2,\"x\":27,\"y\":30},{\"data\":12000000,\"lvl\":2,\"x\":29,\"y\":19},{\"data\":12000001,\"lvl\":0,\"x\":15,\"y\":15},{\"data\":12000001,\"lvl\":0,\"x\":14,\"y\":32},{\"data\":12000005,\"lvl\":1,\"x\":11,\"y\":29},{\"data\":12000005,\"lvl\":1,\"x\":30,\"y\":28},{\"data\":12000002,\"lvl\":1,\"x\":13,\"y\":24}],\"decos\":[],\"respawnVars\":{\"secondsFromLastRespawn\":7200,\"respawnSeed\":561881117,\"obstacleClearCounter\":16,\"time_to_gembox_drop\":5,\"time_in_gembox_period\":1},\"cooldowns\":[],\"newShopBuildings\":[3,0,6,2,6,2,3,1,3,3,125,2,1,2,1,5,0,0,0,0,1,0,0,0,0,0,0,0],\"newShopTraps\":[4,4,1,0,0,2,0,0],\"newShopDecos\":[1,4,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\"last_league_rank\":0,\"last_league_shuffle\":0,\"last_news_seen\":58,\"edit_mode_shown\":false,\"war_tutorials_seen\":0,\"war_base\":false}")  # HomeJSON

        self.writeInt(999)  # ShieldDurationSeconds
        self.writeInt(1)  # DefenseRating
        self.writeInt(1)  # DefenseKFactor

        # LogicClientAvatar

        self.writeInt(0)

        self.writeInt(0)  # DefaultHighID
        self.writeInt(1)  # DefaultLowID
        self.writeInt(0)  # CurrentHomeHighID
        self.writeInt(1)  # CurrentHomeLowID

        self.writeByte(1)  # IsInAlliance

        self.writeInt(0)  # AllianceHighID
        self.writeInt(1)  # AllianceLowID

        self.writeString("SolarLand")  # AllianceName

        self.writeInt(13000001)  # AllianceBadge
        self.writeInt(1)  # AllianceRole

        self.writeByte(0)

        self.writeInt(0)  # LeagueInstanceHighID
        self.writeInt(1)  # LeagueInstanceLowID

        self.writeByte(1)

        self.writeInt(0)  # LastLeagueInstanceHighID
        self.writeInt(1)  # LastLeagueInstanceLowID

        self.writeInt(11)  # LeagueType

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

        self.writeByte(0)

        self.writeInt(0) # CumulativePurchasedDiamonds

        ### ARAYS ###

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