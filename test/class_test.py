#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test class'

__author__ = 'Will Wang'

class Student(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        if self.age >= 18:
            return '成年'
        else:
            return '未成年'

wang = Student('Will Wang', 17)
print(wang.name, wang.age)
print(wang.get_age())
