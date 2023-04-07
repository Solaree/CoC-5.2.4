from Packets.Messages.Client.Login import Login
from Packets.Messages.Client.KeepAlive import KeepAlive
from Packets.Messages.Client.SearchAlliances import SearchAlliances
from Packets.Messages.Client.CreateAlliance import CreateAlliance
from Packets.Messages.Client.ChangeAllianceSettings import ChangeAllianceSettings
from Packets.Messages.Client.ChatToAllianceStream import ChatToAllianceStream
from Packets.Messages.Client.AskForAllianceStream import AskForAllianceStream
from Packets.Messages.Client.AskForAllianceData import AskForAllianceData
from Packets.Messages.Client.AskForJoinableAlliancesList import AskForJoinableAlliancesList
from Packets.Messages.Client.AskForAllianceUnitDonations import AskForAllianceUnitDonations


availablePackets = {

    10101: Login,
    10108: KeepAlive,
    14301: CreateAlliance,
    14302: AskForAllianceData,
    14303: AskForJoinableAlliancesList,
    14305: AskForAllianceStream,
    14309: AskForAllianceUnitDonations,
    14315: ChatToAllianceStream,
    14316: ChangeAllianceSettings,
    14324: SearchAlliances
    
}