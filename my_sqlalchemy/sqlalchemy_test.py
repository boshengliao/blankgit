#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'      #需要事先有user表，或者通过mysql语句创建表，且表中‘无须’表现出‘外键’关系
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    
    books = relationship('Book')
    
    def __repr__(self):     #用以返回‘具体值’，没有此定制类，查询返回的是‘内存地址’，return语句严格按下面‘格式’
        return '<id: %s, name: %s, books: %s>' % (self.id, self.name, self.books)
        
class Book(Base):       
    __tablename__ = 'book'      #需要事先有user表，或者通过mysql语句创建表，且表中‘无须’表现出‘外键’关系
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))
    
    def __repr__(self):
        return '<id: %s, name: %s, user_id: %s>' % (self.id, self.name, self.user_id)
        
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test2')
DBSession = sessionmaker(bind=engine)
'''
session = DBSession()
#new_user = User(id='5', name='Bob')    #插入数据,类似select语句
#session.add(new_user)      #用于提交插入数据，类似mysql中cursor.rowcount

new_book = Book(id='4', name='America', user_id='2')
#new_book2 = Book(id='2', name='Chniese', user_id='1')
session.add(new_book)
#session.add(new_book2)
session.commit()    #类似mysql中conn.commit()
session.close()
'''

session = DBSession()
user = session.query(User).filter(User.id=='1').one()   #查询语句
print(user.books)
print('type: ', type(user))
#print('name: ', user)
#print('id: ', user.books)
session.close()     #关闭连接