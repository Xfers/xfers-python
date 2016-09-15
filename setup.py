import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = []

if sys.version_info < (2, 6):
    warnings.warn(
        'Python 2.5 is no longer officially supported by Xfers. '
        'If you have any questions, please file an issue on Github or '
        'contact us at support@xfers.io.',
        DeprecationWarning)
    install_requires.append('requests >= 0.8.8, < 0.10.1')
    install_requires.append('ssl')
else:
    install_requires.append('requests >= 0.8.8')


# Don't import xfers module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'xfers'))
version_file = open(os.path.join(os.path.dirname(__file__), 'VERSION'))
VERSION = version_file.read().strip()

# Get simplejson if we don't already have json
# if sys.version_info < (3, 0):
#     try:
#         from util import json
#     except ImportError:
#         install_requires.append('simplejson')


setup(
    name='xfers',
    cmdclass={'build_py': build_py},
    version=VERSION,
    description='Xfers python bindings',
    author='Xfers',
    author_email='support@xfers.io',
    url='https://github.com/Xfers/xfers-python',
    packages=['xfers'],
    install_requires=install_requires
)