#!/usr/bin/env python3
# -*-coding: utf-8-*-

import re
print(re.match(r'\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
print(re.split(r'\s+', 'a b     c             d'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-61610202')
print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
