from websocket import create_connection


class WebSocketClientKeywords:

    def connect(self, URL, timeout=None, **options):
        return create_connection(URL, timeout, **options)

    def gettimeout(self, websocket):
        return websocket.gettimeout()

    def settimeout(self, websocket, timeout):
        websocket.settimeout(timeout)

    def getsubprotocol(self, websocket):
        return websocket.getsubprotocol()

    def getstatus(self, websocket):
        return websocket.getstatus()

    def getheaders(self, websocket):
        return websocket.getheaders()

    def send(self, websocket, message):
        return websocket.send(message)

    def send_binary(self, websocket, payload):
        return websocket.send_binary(payload)

    def ping(self, websocket, payload=""):
        websocket.ping(payload)

    def pong(self, websocket, payload=""):
        websocket.pong(payload)

    def recv(self, websocket):
        return websocket.recv()

    def recv_data(self, websocket, control_frame=False):
        return websocket.recv_data(control_frame)

    def send_close(self, websocket):
        websocket.send_close()

    def send_close_with_reason(self, websocket, status, reason):
        websocket.send_close(status, reason)

    def close(self, websocket):
        websocket.close()

    def close_with_reason(self, websocket, status, reason):
        websocket.close(status, reason)
