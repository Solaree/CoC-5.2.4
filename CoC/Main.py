import socket
import time
import os
import binascii
import json
import traceback
from threading import *
from Packets.MessageFactory import *
from Logic.Device import Device


class ServerThread():
    def __init__(self, ip, port):
        self.address = str(ip)
        self.port = int(port)
        self.client = socket.socket()

    def start(self):
        self.client.bind((self.address, self.port))

        print(f'Server is listening on {self.address}:{self.port}'.format(self.address, self.port))

        while True:
            self.client.listen(5)
            client, address = self.client.accept()

            print('New connection from {}'.format(address[0]))
            clientThread = ClientThread(client).start()


class ClientThread(Thread):
    def __init__(self, client):
        Thread.__init__(self)

        self.client = client
        self.device = Device(self.client)

    def recvall(self, size):
        data = []
        while size > 0:
            self.client.settimeout(5.0)
            s = self.client.recv(size)
            self.client.settimeout(None)
            if not s:
                raise EOFError
            data.append(s)
            size -= len(s)
        return b''.join(data)

    def run(self):
        while True:
            header   = self.client.recv(7)
            packetid = int.from_bytes(header[:2], 'big')
            length   = int.from_bytes(header[2:5], 'big')
            version  = int.from_bytes(header[5:], 'big')
            data     = self.recvall(length)

            if len(header) >= 7:
                if length == len(data):
                    print('[*] {} received'.format(packetid))

                    try:
                        decrypted = self.device.decrypt(data)
                        if packetid in availablePackets:

                            Message = availablePackets[packetid](decrypted, self.device)

                            Message.decode()
                            Message.process()

                        else:
                            print('[*] {} not handled'.format(packetid))

                    except:
                            print('[*] Error while decrypting / handling {}'.format(packetid))
                            traceback.print_exc()
                else:
                    print('[*] Incorrect Length for packet {} (header length: {}, data length: {})'.format(packetid, length, len(data)))
            else:
                print('[*] Received an invalid packet from client')
                self.client.close()
if __name__ == '__main__':
	server = ServerThread("0.0.0.0", 9339)
	server.start()