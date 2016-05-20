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

#def _odd_iter():
#    n = 1
#    while True:
#        n = n +2
#        yield n

#def _not_divisible(n):
#    return lambda x: x % n > 0

#def primes():
#    yield 2
#    it = _odd_iter()
#    while True:
#        n = next(it)
#        yield n
#        it = filter(_not_divisible(n), it)

#for n in primes():
#    if n < 1000:
#        print(n)
#    else:
#        break

#def is_palindrome(x):
#    return str(x) == str(x)[::-1] #切片
#output = filter(is_palindrome, range(1, 1000))
#print(list(output))

#sorted函数，用于排序，可接收一个key传入的函数作用在每一个值上
#print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower)) #忽略大小写
#print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True)) #忽略大小写并倒序

#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#def by_name(t):
#    return t[0]
#print(sorted(L, key = by_name))
#def by_score(t):
#    return t[1]
#print(sorted(L, key = by_score, reverse = True))

#返回函数
#def lazy_sum(*args):
#    def sum():
#        ax = 0
#        for n in args:
#            ax = ax + n
#        return ax
#    return sum
#f = lazy_sum(1,2,3,4,5)
#print(f())

#def count():
#    def f(j):
#        def g():
#            return j *j
#        return g
#    fs = []
#    for i in range(1, 4):
#        fs.append(f(i))
#    return fs
#f1, f2, f3 = count()
#print(f1(), f2(), f3())

#匿名函数lambda
#f = lambda x, y: x + y
#print(f(1,2))

#装饰器
#def log(func):
#    def wrapper(*args, **kw):
#        print('call %s():' % func.__name__)
#        return func(*args, **kw)
#    return wrapper
#@log
#def now(month, day):
#    print('2016-%s-%s' % (month, day))
#now('05', '19')

#def log(text):
#    def decorator(func):
#        def wrapper(*args, **kw):
#            print('%s %s():' % (text, func.__name__))
#            return func(*args, **kw)
#        return wrapper
#    return decorator
#@log('execute')
#def now(month, day):
#    print('2016-%s-%s' % (month, day))
#now('05', '19')

#import functools
#def log(func):
#    @functools.wraps(func)
#    def wrapper(*args, **kw):
#        print('begin call %s():' % func.__name__)
#        func(*args, **kw)
#        print('end call %s():' % func.__name__)
#    return wrapper

#@log
#def now(month, day):
#    print('2016-%s-%s' % (month, day))
#now('05', '19')

#偏函数
#import functools
#int2 = functools.partial(int, base=2)
#print(int2('1000000'))
