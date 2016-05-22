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
print(os.path.split('/home/willwang/test/learn_python/test/io_test.txt'))
