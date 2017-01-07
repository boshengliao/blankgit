#!/usr/bin/env python3
#-*- coding: utf-8 -*-

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select * from user')    #执行sql语句获取表user中所有数据
    values = cursor.fetchall()      #将SQL语句中拿到的list含tuple的数据集赋值给values
    def low_list(values):       #构造函数从tuple里取出int数据，可简化为lambda x: x[2]
        return values[2]
    values.sort(key=low_list)   #将数据集按照传入的函数，按分数从低到高排序
    l = []                      #创建list存学生的名字
    try:                        #为了正常关闭数据库，引用try...except...finally...格式，确保正确关闭数据库
        for i in values:        #将数据集里的tuple从list中迭代出来
            if low <= i[2] <= high:     #将tuple中的分数与分数段进行比较，满足条件，则将学生的名字传入l中
                l.append(i[1])
            else:
                print('Hi')
    finally:
        cursor.close()
        conn.commit()
        conn.close()
        return l        #返回满足条件学生的list名单
