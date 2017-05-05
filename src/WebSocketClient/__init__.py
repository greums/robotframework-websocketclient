from .keywords import WebSocketClientKeywords
from .version import get_version

__version__ = get_version()


class WebSocketClient(WebSocketClientKeywords):

    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
