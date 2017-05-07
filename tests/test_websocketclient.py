import sys
sys.path.append('src')

from WebSocketClient import WebSocketClient


def test_connect():
    ws = WebSocketClient()
    ws.connect('ws://echo.websocket.org')


def test_gettimeout():
    pass


def test_settimeout():
    pass


def test_getsubprotocol():
    pass


def test_getstatus():
    pass


def test_getheaders():
    pass


def test_send():
    pass


def test_send_binary():
    pass


def test_ping():
    pass


def test_pong():
    pass


def test_recv():
    pass


def test_recv_data():
    pass


def test_send_close():
    pass
