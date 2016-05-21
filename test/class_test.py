#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test class'

__author__ = 'Will Wang'

class Student(object):
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        if 0 <= self.__age <=100:
            return self.__age
        else:
            return '错误的年龄区间'

    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            return '错误的年龄区间' 

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

#wang = Student('Will Wang', 101)
#print(wang.get_name(), wang.get_age())
#wang.set_name('Yang')
#wang.set_age(102)
#print(wang.get_name(), wang.get_age())
#print(wang._Student__name, wang._Student__age) #私有变量也可以通过"_类名__变量名"的方式调用，但不推荐这样使用，以保证程序的健壮

class Animal(object):

    def run(self):
        print("动物在跑")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

#dog = Dog()
#dog.run()
#cat = Cat()
#cat.run()
#print(dir(dog))

class Students(object):

#    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return 'Students object (name=%s) (age=%s)' % (self._name, self._age)
        __str__ = __repr__
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('请填写整数类型')
        if age > 100 or age < 0:
            raise ValueError('取值范围0~100')
        self._age = age

#wang = Students('wang', 20)
#print(Students('wang', 20))
#wang.age = 20
#print(wang.age)

class Screen(object):

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if isinstance(value, int) and value >= 0:
            self._width = value
        else:
            raise ValueError('长度必须为正整数')

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if isinstance(value, int) and value >= 0:
            self._height = value
        else:
            raise ValueError('高度必须为正整数')

    @property
    def resolution(self):
        return self._width * self.height

#scr = Screen()
#scr.width = 1024
#scr.height = 768
#print('分辨率为：%s' % scr.resolution)

#枚举类
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 7
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#print(Weekday.Mon)
#print(Weekday.Mon.value)
#print(Weekday(7))

#type()动态创建类和元类
def fn(self, name='world'):
    print('Hello, %s!' % name)
Hello = type('Hello', (object,), dict(hello=fn)) #使用type()动态的创建Hello类
h = Hello()
h.hello()
