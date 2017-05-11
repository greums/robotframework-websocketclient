from websocket import create_connection


class WebSocketClientKeywords(object):

    @staticmethod
    def connect(url, timeout=None, **options):
        return create_connection(url, timeout, **options)

    @staticmethod
    def gettimeout(websocket):
        return websocket.gettimeout()

    @staticmethod
    def settimeout(websocket, timeout):
        websocket.settimeout(timeout)

    @staticmethod
    def getsubprotocol(websocket):
        return websocket.getsubprotocol()

    @staticmethod
    def getstatus(websocket):
        return websocket.getstatus()

    @staticmethod
    def getheaders(websocket):
        return websocket.getheaders()

    @staticmethod
    def send(websocket, message):
        return websocket.send(message)

    @staticmethod
    def send_binary(websocket, payload):
        return websocket.send_binary(payload)

    @staticmethod
    def ping(websocket, payload=""):
        websocket.ping(payload)

    @staticmethod
    def pong(websocket, payload=""):
        websocket.pong(payload)

    @staticmethod
    def recv(websocket):
        return websocket.recv()

    @staticmethod
    def recv_data(websocket, control_frame=False):
        return websocket.recv_data(control_frame)

    @staticmethod
    def send_close(websocket):
        websocket.send_close()

    @staticmethod
    def send_close_with_reason(websocket, status, reason):
        websocket.send_close(status, reason)

    @staticmethod
    def close(websocket):
        websocket.close()

    @staticmethod
    def close_with_reason(websocket, status, reason):
        websocket.close(status, reason)
