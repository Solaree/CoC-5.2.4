import traceback

from CryptoRC4.Crypto import CryptoRc4
from Packets.MessageFactory import *


class Device:

    AndroidID = None
    DeviceModel = None
    OpenUDID = None
    OSVersion = None
    IsAndroid = False
    Language = None

    def __init__(self, socket=None):

        self.socket = socket
        self.crypto = CryptoRc4()

    def SendData(self, ID, data, version=None):

        encrypted = self.crypto.encrypt(data)
        packetID   = ID.to_bytes(2, 'big')

        if version:
            packetVersion = version.to_bytes(2, 'big')

        else:
            packetVersion = (0).to_bytes(2, 'big')

        if self.socket is None:
            self.transport.write(packetID + len(encrypted).to_bytes(3, 'big') + packetVersion + encrypted)

        else:
            self.socket.send(packetID + len(encrypted).to_bytes(3, 'big') + packetVersion + encrypted)

        print('[*] {} sent'.format(ID))

    def decrypt(self, data):
        return self.crypto.decrypt(data)

    def processPacket(self, packetID, payload):

        print('[*] {} received'.format(packetID))

        try:
            decrypted = self.decrypt(payload)

            if packetID in availablePackets:

                Message = availablePackets[packetID](decrypted, self)
                Message.decode()
                Message.process()

            else:
                print('[*] {} not handled'.format(packetID))

        except:
            print('[*] Error while decrypting / handling {}'.format(packetID))
            traceback.print_exc()