#!/usr/bin/env python3
# -*-coding: utf-8 -*-

'a test thread and multiprocessing'

__author__ = 'Will Wang'

import os
print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('这是子进程ID%s，父进程ID%s' % (os.getpid(), os.getppid()))
else:
    print('这是父进程ID%s，子进程ID%s' % (os.getpid(), pid))