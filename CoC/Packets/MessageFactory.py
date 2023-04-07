from Packets.Messages.Client.Login import *
from Packets.Messages.Client.KeepAlive import *
from Packets.Messages.Client.EndClientTurn import *
from Packets.Messages.Client.SearchAlliances import *
from Packets.Messages.Client.CreateAlliance import *
from Packets.Messages.Client.ChangeAllianceSettings import *
from Packets.Messages.Client.ChatToAllianceStream import *
from Packets.Messages.Client.AskForAllianceStream import *
from Packets.Messages.Client.AskForAllianceData import *
from Packets.Messages.Client.AskForJoinableAlliancesList import *
from Packets.Messages.Client.AskForAllianceUnitDonations import *


availablePackets = {

    10101: Login,
    10108: KeepAlive,
    14102: EndClientTurn,
    14301: CreateAlliance,
    14302: AskForAllianceData,
    14303: AskForJoinableAlliancesList,
    14305: AskForAllianceStream,
    14309: AskForAllianceUnitDonations,
    14315: ChatToAllianceStream,
    14316: ChangeAllianceSettings,
    14324: SearchAlliances
    
}