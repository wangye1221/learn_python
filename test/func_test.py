#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#递归函数，这种方式如果n的数值过大会造成栈溢出
#def fact(n):
#    if n==1:
#        return 1
#    return n * fact(n - 1)
#print(fact(5))

#切片
#L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#print(L[0:3]) #从0开始取三个，0、1、2
#print(L[::2]) #从0开始取所有的，间隔一个
#L = list(range(100))
#print(L[::10])

#列表生成式
#print([x * x for x in range(1, 11)])
#import os
#print([d for d in os.listdir('/home/willwang')])
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])
