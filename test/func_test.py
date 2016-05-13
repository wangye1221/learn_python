#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#递归函数，这种方式如果n的数值过大会造成栈溢出
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
