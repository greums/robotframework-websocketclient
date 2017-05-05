from .keywords import WebSocketClientKeywords
from .version import VERSION

_version_ = VERSION

class WebSocketClient(WebSocketClientKeywords):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
