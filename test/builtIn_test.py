#!/usr/bin/env python3
# -*-coding:utf-8 -*-

'''
from datetime import datetime, timedelta

print(datetime.now())
print(datetime(2016, 5, 30, 12, 21))
print(datetime(2016, 5, 30, 12, 21).timestamp())
print(datetime.fromtimestamp(1464582060.0))
print(datetime.utcfromtimestamp(1464582060.0))
print(datetime.strptime('2016-05-30 12:21:30', '%Y-%m-%d %H:%M:%S'))
print(datetime.now().strftime('%a, %b %d %H:%M'))

print(datetime.now() + timedelta(hours=10))
print(datetime.now() - timedelta(days=1))
print(datetime.now() + timedelta(days=1, hours=24))
'''

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
