############################################################################
#
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import socket


class TcpClient:
    BUFFER_SIZE = 1024 * 128

    #
    def __init__(self, host='127.0.0.1', port=8989):
        self.host = host
        self.port = port
        self.socket = None
        self.connect = False
        self.iserror = True
        self.error = "Socket has not been started!"

    #
    #
    def start(self):
        #
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            self.socket = None
            self.iserror = True
            self.error = "Error: Creating socket!"
        #
        try:
            if self.socket is not None:
                self.socket.connect((self.host, self.port))
                self.connect = True
                self.iserror = False
                self.error = ""
        except:
            self.socket.close()
            self.socket = None
            self.connect = False
            self.iserror = True
            self.error = "Error: Connecting socket!"

    #
    #
    def send(self, data):
        tmp = None
        #
        if not self.iserror:
            if self.socket is not None:
                if self.connect:
                    try:
                        self.socket.send(data)
                        tmp = self.socket.recv(TcpClient.BUFFER_SIZE)
                        if tmp == b'':
                            tmp = None
                            self.iserror = True
                            self.error = "Error: Connection lost! "
                    except:
                        tmp = None
                        self.iserror = True
                        self.error = "Error: Connection lost! "
                else:
                    tmp = None
                    self.iserror = True
                    self.error = "Error: Connection lost! "
            else:
                tmp = None
                self.iserror = True
                self.error = "Error: Connection lost! "
        else:
            tmp = None
            self.iserror = True
            self.error = "Error: Connection lost! "
        #
        return tmp

    #
    #
    def close(self):
        if self.socket is not None:
            if self.connect:
                self.socket.shutdown(socket.SHUT_RDWR)
            #
            try:
                self.socket.close()
                self.socket = None
                self.connect = None
                self.iserror = True
                self.error = "Socket has been closed!"
            except:
                self.socket = None
                self.connect = None
                self.iserror = True
                self.error = "Socket has been closed!"


class TcpServer:
    BUFFER_SIZE = 1024 * 128

    #
    def __init__(self, host='0.0.0.0', port=8989):
        self.host = host
        self.port = port
        self.socket = None
        self.accept_addr = ''
        self.accept_port = 0
        self.accept_obj = None
        self.connect = False
        self.iserror = True
        self.error = "Socket has not been started!"

    #
    #
    def start(self):
        #
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            self.socket = None
            self.iserror = True
            self.error = "Error: Creating socket!"
        #
        try:
            if self.socket is not None:
                self.socket.bind((self.host, self.port))
                self.socket.listen(0)
                self.accept_obj, tmp_addr = self.socket.accept()
                self.accept_addr = tmp_addr[0]
                self.accept_port = tmp_addr[1]
                self.connect = True
                self.iserror = False
                self.error = ""
        except:
            self.socket.close()
            self.socket = None
            self.connect = False
            self.iserror = True
            self.error = "Error: 'bind(), listen(0) and accept() functions'"

    #
    #
    def send(self, data):
        tmp = None
        #
        if not self.iserror:
            if self.socket is not None:
                if self.connect:
                    try:
                        if self.accept_obj is not None:
                            tmp = self.accept_obj.recv(TcpServer.BUFFER_SIZE)
                            #
                            if tmp != b'':
                                self.accept_obj.send(data)
                            else:
                                tmp = None
                                self.accept_addr = ''
                                self.accept_port = 0
                                self.accept_obj = None
                                self.connect = False
                                self.iserror = True
                                self.error = "Error: Connection lost! "

                        else:
                            tmp = None
                            self.accept_addr = ''
                            self.accept_port = 0
                            self.accept_obj = None
                            self.connect = False
                            self.iserror = True
                            self.error = "Error: Connection lost! "
                    except:
                        tmp = None
                        self.accept_addr = ''
                        self.accept_port = 0
                        self.accept_obj = None
                        self.connect = False
                        self.iserror = True
                        self.error = "Error: Connection lost! "
                else:
                    tmp = None
                    self.accept_addr = ''
                    self.accept_port = 0
                    self.accept_obj = None
                    self.connect = False
                    self.iserror = True
                    self.error = "Error: Connection lost! "
            else:
                tmp = None
                self.accept_addr = ''
                self.accept_port = 0
                self.accept_obj = None
                self.connect = False
                self.iserror = True
                self.error = "Error: Connection lost! "
        else:
            tmp = None
            self.accept_addr = ''
            self.accept_port = 0
            self.accept_obj = None
            self.connect = False
            self.iserror = True
            self.error = "Error: Connection lost! "
        #
        return tmp

    #
    #
    def close(self):
        if self.socket is not None:
            if self.connect:
                try:
                    self.accept_obj.shutdown(socket.SHUT_RDWR)
                    self.socket.shutdown(socket.SHUT_RDWR)
                except:
                    pass
            #
            try:
                self.socket.close()
                self.socket = None
                self.connect = None
                self.accept_obj = None
                self.accept_addr = ''
                self.accept_port = 0
                self.iserror = True
                self.error = "Socket has been closed!"
            except:
                self.socket = None
                self.connect = None
                self.accept_obj = None
                self.accept_addr = ''
                self.accept_port = 0
                self.iserror = True
                self.error = "Socket has been closed!"


class UdpClient:
    BUFFER_SIZE = 1024 * 128

    #
    def __init__(self, host='127.0.0.1', port=8989):
        self.host = host
        self.port = port
        self.socket = None
        self.iserror = True
        self.recevie_addr = ''
        self.recevie_port = 0
        self.error = "Socket has not been started!"

    #
    #
    #
    def start(self):
        #
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.iserror = False
            self.error = ""
            self.recevie_addr = ''
            self.recevie_port = 0
        except:
            self.socket = None
            self.iserror = True
            self.error = "Error: Creating socket!"
            self.recevie_addr = ''
            self.recevie_port = 0
        #

    #
    #
    def send(self, data):
        tmp_data = None
        #
        if not self.iserror:
            if self.socket is not None:
                try:
                    self.socket.sendto(data, (self.host, self.port))
                    tmp = self.socket.recvfrom(UdpClient.BUFFER_SIZE)
                    #
                    if tmp is not None:
                        if tmp[0] == b'' or tmp[0] is None:
                            tmp = None
                            self.iserror = True
                            self.error = "Socket has been closed!"
                            self.recevie_addr = ''
                            self.recevie_port = 0
                        else:
                            tmp_data = tmp[0]
                            self.recevie_addr = tmp[1][0]
                            self.recevie_port = tmp[1][1]

                    else:
                        tmp = None
                        self.iserror = True
                        self.error = "Socket has been closed!"
                        self.recevie_addr = ''
                        self.recevie_port = 0
                #
                except:
                    self.iserror = True
                    self.error = "Socket has been closed!"
                    self.recevie_addr = ''
                    self.recevie_port = 0
        #
        return tmp_data

    #
    def close(self):
        if self.socket is not None:
            #
            try:
                self.socket.close()
                self.socket = None
                self.iserror = True
                self.error = "Socket has been closed!"
            except:
                self.socket = None
                self.iserror = True
                self.error = "Socket has been closed!"


class UdpServer:
    BUFFER_SIZE = 1024 * 128

    #
    def __init__(self, host='0.0.0.0', port=8989):
        self.host = host
        self.port = port
        self.socket = None
        self.iserror = True
        self.recevie_addr = ''
        self.recevie_port = 0
        self.error = "Socket has not been started!"

    #
    #
    #
    def start(self):
        #
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.iserror = False
            self.error = ""
            self.recevie_addr = ''
            self.recevie_port = 0
        except:
            self.socket = None
            self.iserror = True
            self.error = "Error: Creating socket!"
            self.recevie_addr = ''
            self.recevie_port = 0

        try:
            self.socket.bind((self.host, self.port))
            self.iserror = False
            self.error = ""
            self.recevie_addr = ''
            self.recevie_port = 0
        except:
            self.socket = None
            self.iserror = True
            self.error = "Error: 'Bind() function' "
            self.recevie_addr = ''
            self.recevie_port = 0
        #

    #
    #
    def send(self, data):
        tmp_data = None
        #
        if not self.iserror:
            if self.socket is not None:
                try:
                    tmp = self.socket.recvfrom(UdpServer.BUFFER_SIZE)
                    #
                    if tmp is not None:
                        if tmp[0] == b'' or tmp[0] is None:
                            tmp = None
                            self.iserror = True
                            self.error = "Socket has been closed!"
                            self.recevie_addr = ''
                            self.recevie_port = 0
                        else:
                            tmp_data = tmp[0]
                            self.recevie_addr = tmp[1][0]
                            self.recevie_port = tmp[1][1]
                            #
                            self.socket.sendto(data, (self.recevie_addr, self.recevie_port))
                    else:
                        tmp = None
                        self.iserror = True
                        self.error = "Socket has been closed!"
                        self.recevie_addr = ''
                        self.recevie_port = 0
                #
                except:
                    self.iserror = True
                    self.error = "Socket has been closed!"
                    self.recevie_addr = ''
                    self.recevie_port = 0
        #
        return tmp_data

    #
    def close(self):
        if self.socket is not None:
            #
            try:
                self.socket.close()
                self.socket = None
                self.iserror = True
                self.error = "Socket has been closed!"
            except:
                self.socket = None
                self.iserror = True
                self.error = "Socket has been closed!"


#
#
class Win32Socket:
    #
    #
    def __init__(self, win32crypto, protocol="UDP", host='0.0.0.0', port=8989):
        self.protocol = protocol.upper()
        self.host = host
        self.port = port
        self.authentication = False
        self.win32crypto = win32crypto
        self.connection = False
        self.receive_addr = ""
        self.receive_port = 0
        if protocol.upper() == "UDP":
            if host == '0.0.0.0':
                self.socket = UdpServer(host=host, port=port)
                self.iserror = self.socket.iserror
                self.error = self.socket.error
            else:
                self.socket = UdpClient(host=host, port=port)
                self.iserror = self.socket.iserror
                self.error = self.socket.error
        elif protocol.upper() == "TCP":
            if host == '0.0.0.0':
                self.socket = TcpServer(host=host, port=port)
                self.iserror = self.socket.iserror
                self.error = self.socket.error
            else:
                self.socket = TcpClient(host=host, port=port)
                self.iserror = self.socket.iserror
                self.error = self.socket.error
        else:
            self.socket = None
            self.iserror = True
            self.error = "Error: 'Protocol's entry is incorrect"

    #
    #
    def start(self,settimeout):
        if self.socket is not None:
            if self.protocol == 'UDP':
                if self.host == '0.0.0.0':
                    self.socket.start()
                    self.iserror = self.socket.iserror
                    self.error = self.socket.error
                    try:
                        if settimeout != 0:
                            self.socket.socket.settimeout(settimeout)
                    except:
                        self.iserror = True
                        self.error = "Error: settimeout function()"
                    if not self.iserror:
                        self.send(b' ')
                        self.iserror = self.socket.iserror
                        self.error = self.socket.error
                        if not self.iserror:
                            self.connection = True
                            self.receive_addr = self.socket.recevie_addr
                            self.receive_port = self.socket.recevie_port
                else:
                    self.socket.start()
                    self.iserror = self.socket.iserror
                    self.error = self.socket.error
                    try:
                        if settimeout != 0:
                            self.socket.socket.settimeout(settimeout)
                    except:
                        self.iserror = True
                        self.error = "Error: settimeout function()"
                    if not self.iserror:
                        self.send(b' ')
                        self.iserror = self.socket.iserror
                        self.error = self.socket.error
                        if not self.iserror:
                            self.connection = True
                            self.receive_addr = self.socket.recevie_addr
                            self.receive_port = self.socket.recevie_port

            elif self.protocol == "TCP":
                if self.host == '0.0.0.0':
                    self.socket.start()
                    self.iserror = self.socket.iserror
                    self.error = self.socket.error
                    try:
                        if settimeout != 0:
                            self.socket.socket.settimeout(settimeout)
                    except:
                        self.iserror = True
                        self.error = "Error: settimeout function()"
                    if not self.iserror:
                        self.send(b' ')
                        self.iserror = self.socket.iserror
                        self.error = self.socket.error
                        if not self.iserror:
                            self.receive_addr = self.socket.accept_addr
                            self.receive_port = self.socket.accept_port
                            self.connection = True
                else:
                    self.socket.start()
                    self.iserror = self.socket.iserror
                    self.error = self.socket.error
                    try:
                        if settimeout != 0:
                            self.socket.socket.settimeout(settimeout)
                    except:
                        self.iserror = True
                        self.error = "Error: settimeout function()"
                    if not self.iserror:
                        self.send(b' ')
                        self.iserror = self.socket.iserror
                        self.error = self.socket.error
                        if not self.iserror:
                            self.receive_addr = self.host
                            self.receive_port = self.port
            else:
                self.socket = None
                self.iserror = True
                self.error = "Error: 'Protocol's entry is incorrect"

    #
    #
    def send(self, data):
        res = None
        if not self.iserror:
            isnormal0, data = self.win32crypto.encrypt(data)
            if isnormal0:
                res = self.socket.send(data)
                self.iserror = self.socket.iserror
                self.error = self.socket.error
            else:
                self.iserror = True
                self.error = 'Error: Win32Crtypto function()'
            #
            if self.protocol == 'UDP':
                if not self.iserror:
                    self.receive_addr = self.socket.recevie_addr
                    self.receive_port = self.socket.recevie_port
            #
            if self.iserror:
                self.connection = False
                self.authentication = False
            else:
                self.connection = True
                #
                isnormal, res = self.win32crypto.decrypt(res)
                if isnormal:
                    self.authentication = True
                else:
                    self.authentication = False
        else:
            self.connection = False
            self.authentication = False
        #
        return res

    #
    #
    def close(self):
        self.socket.close()
        self.iserror = self.socket.iserror
        self.error = self.socket.error
