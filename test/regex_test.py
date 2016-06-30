#!/usr/bin/env python3
# -*-coding: utf-8-*-

'''
import re
print(re.match(r'\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
print(re.split(r'\s+', 'a b     c             d'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-61610202')
print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
'''
'''
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print('MD5: %s' % md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print('SHA1: %s' % sha1.hexdigest())
'''

import hashlib

db = {}

def get_md5_salt(usr, pwd):
    md5 = hashlib.md5()
    md5.update((pwd + usr + 'the-Salt').encode('utf-8'))
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5_salt(username, password)
    return '注册成功'

def login(username, password):
    login = False
    try:
        if db[username] == get_md5_salt(username, password):
            login = True
        else:
            login = False
    except KeyError as e:
        login = False
    finally:
        return login

if __name__ == '__main__':
    while True:
        print('注册请输入：1，登录请输入：2，退出请输入：0')
        mode = input()
        if mode == '0':
            break
        elif mode == '1':
            username = input('请输入帐号')
            password = input('请输入密码')
            password2 = input('请再次输入密码')
            if password != password2:
                print('两次输入的密码不相同')
            else:
                print(register(username, password))
        elif mode == '2':
            username = input('请输入帐号')
            password = input('请输入密码')
            if login(username, password):
                print('登录成功')
            else:
                print('登录失败')
        else:
            print('请输入正确的命令')