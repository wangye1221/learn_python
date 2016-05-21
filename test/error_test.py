#!/usr/bin/env python3
# -*-coding: utf-8 -*-

'a test error'

__author__ = 'Will Wang'

import logging
import pdb
#logging.basicConfig(level=logging.INFO)

try:
    print('try..........')
    pdb.set_trace()
    logging.info('This is logging.info')
    r = 10 / 0
    print('result = %s' % r)
except Exception as e:
#    print('except:', e)
    logging.exception(e)
finally:
    print('finally..........')
print('END')
