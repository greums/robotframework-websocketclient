import sys

sys.path.append('src')

from WebSocketClient import WebSocketClient

WEBSOCKET_URL = 'ws://echo.websocket.org'


class TestWebSocketClient(object):

    def setup_class(self):
        self.sock = WebSocketClient()
        self.ws = self.sock.connect(WEBSOCKET_URL)

    def test_connect(self):
        self.sock.connect(WEBSOCKET_URL)

    def test_gettimeout(self):
        pass

    def test_settimeout(self):
        pass

    def test_getsubprotocol(self):
        pass

    def test_getstatus(self):
        pass

    def test_getheaders(self):
        pass

    def test_send(self):
        self.sock.send(self.ws, 'Hello, world')

    def test_send_binary(self):
        pass

    def test_ping(self):
        pass

    def test_pong(self):
        pass

    def test_recv(self):
        self.sock.send(self.ws, 'Hello, world')
        data = self.sock.recv(self.ws)
        assert data == 'Hello, world'

    def test_recv_data(self):
        pass

    def test_send_close(self):
        pass
