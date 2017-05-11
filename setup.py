import codecs
import io
import re
from os.path import abspath, dirname, join

from setuptools import setup, find_packages

LIBRARY_NAME = 'WebSocketClient'
CWD = abspath(dirname(__file__))


def read(*names, **kwargs):
    with io.open(join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^VERSION = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


VERSION = find_version(join(CWD, 'src', LIBRARY_NAME), "version.py")

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
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
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
