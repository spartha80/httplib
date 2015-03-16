#!/usr/bin/python
current_milli_time = lambda: int(round(time.time() * 1000))

class HttpConnection:
    def __init__(self, remotehost, rport, localhost, lport):
        self.remotehost = remotehost
        self.rport = rport
        self.localhost = localhost
        self.lport = lport
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(0)
        self.s.connect((self.rhost, self.rport))

    def get(self, httpRequest):

    def close(self):
        self.s.shutdown()
        self.s.close()


class HttpClient:
    def __init__(self, max_client=None):
        if max_client == None:
            self.max_client = 100
        else:
            self.max_client = max_client

HttpRequestDispatcher globalDispatcher = HttpRequestDispatcher()

class HttpRequestDispatcher:
    def __init_(self):
        self.max_client = 10
        self.requestQueue = collections.deque()
        self.partialRequestQ = {} #Dictionary
        self.connections = []
        self.socketList = []
        self.requestListLock = Lock()

    def getGlobalDispatcher():
        return globalDispatcher

    def initConnections(self, remotehost, rport, localhost, lport):
        for i in range(self.max_client):
            conn = HttpConnection(remotehost, rport, localhost, lport)
            self.connections[i] = conn
            self.socketList[i] = conn.s

    def cleanUp(self):
        for i in range(self.max_client):
            self.connections[i].close()

    def setMaxClients(self, max_clients):
        self.max_clients = max_clients

    def addRequest(self, request, count):
        self.requestListLock.acquire()
        for i in range(count)
            self.requestQueue.append(request)
        self.requestListLock.release()

    def getNextRequest(self):
        self.requestListLock.acquire()
        if self.requestQueue.len() != 0:
            return self.requestQueue.popleft()
        self.requestListLock.release()

    def addPartialRequest(self, request):
        self.requestQueue.append(request)

    def getPartialRequest(self, request):
        if self.requestQueue.len() != 0:
            return self.requestQueue.popleft()

    def sendPartialMessage(self, sock):
        requestMsg = partialRequestQ[sock]
        totalsent = 0
        msgSize = len(requestMsg.len)
        while totalsent < msgSize:
            sent = sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            if sent in (errno.EWOULDBLOCK, errno.EAGAIN):
                del partialRequestQ[sock]
                partialRequestQ[sock] = msg[totalsent:]
                return errno.EWOULDBLOCK
            totalsent = totalsent + sent
        if totalsent == msgSize:
            del partialRequestQ[sock]
        return totalsent

    def sendMessage(self, sock):
        reqMessage = getNextRequest().getTSMessage()
        msgSize = len(reqMessage)
        msgSent = 0
        while msgSent < msgSize:
            sent = sock.send(reqMessage[msgSent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            if sent in (errno.EWOULDBLOCK, errno.EAGAIN):
                partialRequestQ[sock] = reqMessage[msgSent:]
                return errno.EWOULDBLOCK
            msgSent = msgSent + sent
        return msgSent

    def doSelect(self):
        ready_to_read, ready_to_write, in_error = \
               select.select(
                  self.socketList,
                  self.socketList,
                  [],
                  60)
        if len(ready_to_write) != 0:
            for sock in ready_to_write:
                if sock in partialRequestQ:
                    if sendPartialMessage(sock) != errno.EWOULDBLOCK:
                        sendMessage(sock)
                else:
                    while True:
                        ret = sendMessage(sock)
                        if ret == errno.EWOULDBLOCK:
                            break
        if len(ready_to_read) != 0:
            for sock in ready_to_read:



class HttpRequest:
    def __init__(self, url, verb):
        self.url = url
        self.verb = verb
        p = urlparse(url)
        self.host = p.hostname
        self.port = p.port
        self.resource = p.path
        self.requestMessage = verb," ",self.resource," HTTP/1.1","User-Agent: loadTest","Host:",self.host,"Accept: */*","Connection:keep-alive"

    def getVerb(self):
        return self.verb

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port

    def getResource(self):
        return self.resource

    def getTSMessage(self):
        return self.requestMessage,"ts1:",current_milli_time(),"\r\n\r\n"
