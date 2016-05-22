#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test IO'

__author__ = 'Will Wang'

'''
with open('/home/willwang/test/learn_python/test/io_test.txt', 'r') as f:
    print(f.read())

with open('/home/willwang/test/learn_python/test/io_test.txt', 'a') as f:
    f.write('这段文字是写进去的')

with open('/home/willwang/test/learn_python/test/io_test.txt', 'r') as f:
    print(f.read())
'''

import os

#print(os.name)
#print(os.uname())
#print(os.environ.get('PATH'))
#print(os.path.abspath('.'))
#print(os.path.split('/home/willwang/test/learn_python/test/io_test.txt'))

#json

import json
'''
d = dict(name='Bob', age=20, score=88)
with open('io_test.txt', 'w') as f:
    json.dump(d, f)
with open('io_test.txt', 'r') as f:
    print(json.load(f))
'''

class Student(object):
    def __init__(self, name, age, score):
        self._name = name
        self._age = age
        self._score = score
s = Student('Bob', 20, 100)
print(json.dumps(s, default=lambda obj: obj.__dict__))
