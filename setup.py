import codecs
from os.path import abspath, dirname, join

from setuptools import setup, find_packages

LIBRARY_NAME = 'WebSocketClient'
CWD = abspath(dirname(__file__))
VERSION_PATH = join(CWD, 'src', LIBRARY_NAME, 'version.py')
exec (compile(open(VERSION_PATH).read(), VERSION_PATH, 'exec'))

with codecs.open(join(CWD, 'README.rst'), encoding='utf-8') as reader:
    LONG_DESCRIPTION = reader.read()

setup(
    name='robotframework-%s' % LIBRARY_NAME.lower(),
    version=VERSION,
    description='Robot Framework keywords for websocket-client',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/greums/robotframework-websocketclient',
    download_url='https://github.com/greums/robotframework-websocketclient/tarball/%s' % VERSION,
    author='Damien Le Bourdonnec',
    author_email='greumsworkshop@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Robot Framework :: Library',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
    keywords=['robotframework', 'websocket'],
    platforms='any',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'robotframework',
        'websocket-client'
    ],
    include_package_data=True,
    zip_safe=False
)
