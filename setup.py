#!/usr/bin/python

from distutils.core import setup

setup(
    name='zynk',
    description='Simple rsync wrapper to support file transfer over SSL tunnel',
    long_description='zynk is a small rsync wrapper + daemon which on connection establish a SSL tunnel, the server authenticates the client and rsync can be used as usual.',
    platforms='posix',
    version='0.1',
    license='GPLv3 or later',
    url='http://seba-geek.de/projects/zynk/',
    author='Sebastian Lohff',
    author_email='seba@someserver.de',
    scripts=['zynk', 'zynkd'],
)

