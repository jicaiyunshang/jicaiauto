#! /usr/bin/env python
__author__ = 'Tser'
__email__ = '807447312@qq.com'
__project__ = 'jicaiauto'
__script__ = 'config.py'
__create_time__ = '2020/7/15 23:18'

from os import path

class DBCONFIG:
    path = path.dirname(path.abspath(__file__)) + '/../data/jicaiauto.db'