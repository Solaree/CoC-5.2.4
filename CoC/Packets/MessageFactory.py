from Packets.Messages.Client.LoginMessage import *
from Packets.Messages.Client.KeepAliveMessage import *
from Packets.Messages.Client.EndClientTurnMessage import *
from Packets.Messages.Client.SearchAlliancesMessage import *
from Packets.Messages.Client.CreateAllianceMessage import *
from Packets.Messages.Client.ChangeAllianceSettingsMessage import *
from Packets.Messages.Client.ChatToAllianceStreamMessage import *
from Packets.Messages.Client.AskForAllianceDataMessage import *
from Packets.Messages.Client.AskForJoinableAlliancesListMessage import *
from Packets.Messages.Client.AskForAllianceUnitDonationsMessage import *
from Packets.Messages.Client.AskForAvatarProfileMessage import *
#from Packets.Messages.Client.VisitHomeMessage import *
from Packets.Messages.Client.AttackNpcMessage import *
from Packets.Messages.Client.JoinAllianceMessage import *


availablePackets = {

    10101: LoginMessage,
    10108: KeepAliveMessage,
    14102: EndClientTurnMessage,
    14134: AttackNpcMessage,
    14301: CreateAllianceMessage,
    14302: AskForAllianceDataMessage,
    14303: AskForJoinableAlliancesListMessage,
    14305: JoinAllianceMessage,
    14309: AskForAllianceUnitDonationsMessage,
    #14113: VisitedHomeData,
    14315: ChatToAllianceStreamMessage,
    14316: ChangeAllianceSettingsMessage,
    14324: SearchAlliancesMessage,
    14325: AskForAvatarProfileMessage
    
}