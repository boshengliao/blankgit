#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib, time
global db
db = dict(a=1)
def get_md5(username,password):
    information = password + username + 'the Michael'
    user_md5 = hashlib.md5()
    user_md5.update(information.encode('utf-8'))
    return user_md5.hexdigest()
    
def login(username,password):
    if get_md5(username,password) == db[username]:
        print('登陆成功！')
    else:
        print('Failed...')

def register(username,password):
    if username in db:
        print('该账号已被注册...')
    else:
        db[username] = get_md5(username,password)
        print('注册成功...')
        
if __name__ == '__main__':
    print(db)
    name = input('请输入注册账号：')
    password = input('请输入注册密码：')
    register(name,password)
    name1 = input('请输入登陆账号：')
    password1 = input('请输入登陆密码：')
    login(name1,password1)
