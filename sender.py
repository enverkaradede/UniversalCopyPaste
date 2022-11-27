import socket
# import clipboard

# HOST = '127.0.0.1'
# PORT = 12345

# cp = clipboard.Clipboard()

# def SendCopiedTextToServer(text):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((HOST, PORT))
#     s.sendall(bytes(text, encoding='cp1254'))
#     cp.SetText('')
#     cp.CopyText()
#     data = s.recv(1024)

#     print(f'Received data {data.decode(encoding="cp1254")}')


class TCPSender:
    def __init__(self):
        self._host = '127.0.0.1'
        self._port = '12345'
        self._data = None
        self._dataEncoding = ''
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._response = None

    def setHost(self, host):
        self._host = host

    def getHost(self):
        return self._host

    def setPort(self, port):
        self._port = port

    def getPort(self):
        return self._port

    def setData(self, data):
        self._data = data

    def getData(self):
        return self._data

    def setEncoding(self, dataEncoding):
        self._dataEncoding = dataEncoding

    def getEncoding(self):
        return self._dataEncoding

    def _setResponse(self, response):
        self._response = response

    def getResponse(self):
        return self._response

    def connectSocket(self):
        self._socket.connect((self._host, self._port))

    def sendCopiedTextToDevice(self):
        self._socket.sendall(bytes(self._data))

    def receiveResponse(self):
        response = self._socket.recv(1024)
        self._response = response
        print(f'Data received! Received data is {self._response.decode(encoding=self._dataEncoding)}')

    def closeSocket(self):
        self._socket.close()
        print('Connection is closed!')