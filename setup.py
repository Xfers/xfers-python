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
else:
    install_requires.append('requests >= 2.5.4')

# Don't import xfers module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'xfers'))

setup(
    name='xfers',
    cmdclass={'build_py': build_py},
    version='1.3.0',
    description='Xfers python bindings',
    author='Xfers',
    author_email='support@xfers.io',
    url='https://github.com/Xfers/xfers-python',
    packages=['xfers'],
    install_requires=install_requires,
    keywords=['payments', 'xfers'],
    license='MIT',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)