#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'robotframework-websocketclient',
    package_dir  = {'' : 'src'},
    packages = ['WebSocketClient'],
    version = '1.2.1',
    description = '	Robot Framework keywords for websocket-client',
    author = 'Damien Le Bourdonnec',
    author_email = 'damien.lebourdonnec@gmail.com',
    url = 'https://github.com/greums/robotframework-websocketclient',
    download_url = 'https://github.com/greums/robotframework-websocketclient/tarball/1.2.1',
    keywords = ['robotframework', 'websocket'],
    install_requires=[
        'websocket-client'
    ],
    classifiers = []
)
