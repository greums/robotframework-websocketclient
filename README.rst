IMAP email testing library for Robot Framework
==============================================

|Version| |Status| |Python| |Download| |License|

Introduction
------------

WebSocketClient is [Robot Framework](http://code.google.com/p/robotframework/) test library that uses the [websocket-client](https://github.com/liris/websocket-client) module.

Examples
''''''''

.. code:: robotframework

    *** Settings ***
    Library  WebSocketClient

    *** Test Cases ***
    Echo
        ${my_websocket}=  WebSocketClient.Connect  ws://echo.websocket.org
        WebSocketClient.Send  ${my_websocket}  Hello
        ${result}=  WebSocketClient.Recv  ${my_websocket}
        Should Be Equal  Hello  ${result}
        WebSocketClient.Close  ${my_websocket}

Installation
------------

Using ``pip``
'''''''''''''

The recommended installation method is using pip_:

.. code:: console

    pip install robotframework-websocketclient

The main benefit of using ``pip`` is that it automatically installs all
dependencies needed by the library. Other nice features are easy upgrading
and support for un-installation:

.. code:: console

    pip install --upgrade robotframework-websocketclient
    pip uninstall robotframework-websocketclient

Notice that using ``--upgrade`` above updates both the library and all
its dependencies to the latest version. If you want, you can also install
a specific version:

.. code:: console

    pip install robotframework-websocketclient==x.x.x

Usage
-----

To write tests with Robot Framework and WebSocketClient,
WebSocketClient must be imported into your Robot test suite.

.. code:: robotframework

    *** Settings ***
    Library    WebSocketClient

See `Robot Framework User Guide`_ for more information.

More information about Robot Framework standard libraries and built-in tools
can be found in the `Robot Framework Documentation`_.

License
-------

Copyright (c) 2017 Damien Le Bourdonnec
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
