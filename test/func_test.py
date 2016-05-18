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
#L = ['Hello', 'World', 18, 'Apple', None]
#print([s.lower() for s in L if isinstance(s, str)])

# 生成器
#g = (x for x in range(10))
#for n in g:
#    print(n)

#斐波拉契数列和生成器
#def fib(max):
#    n, a, b = 0, 0, 1
#    while n < max:
##        print(b)
#        yield b
#        a, b = b, a + b
#        n = n + 1
#    return 'done'
#for x in fib(10):
#    print(x)

#高阶函数
#def add(a, b, f):
#    return f(a) + f(b)
#print(add(4, -4, abs)) #将函数当作参数传入另一个函数中

#map\reduce函数
#from functools import reduce
#def f(x, y):
#    return x * y
##L = map(f, [1,2,3])
#J = reduce(f, [1,2,3])
#print(J)

#filter函数，用于筛选，返回true\falsh
#def is_odd(x):
#    return x % 2 == 1
#print(list(filter(is_odd, [1,2,3,4,5,6,7])))
#def not_empty(x):
#    return x and x.strip()
#print(list(filter(not_empty, ['1','','2',None,'3','         '])))

def _odd_iter():
    n = 1
    while True:
        n = n +2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

