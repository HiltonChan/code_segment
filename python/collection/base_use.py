#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    列表：
        特点：
            1.可变序列，元素可重新赋值
    元组：
        特点：
            1.不可变序列，元素不可重新赋值
    字典：
        特点：
            1.key value存储
"""

print '---------- list start ----------'

#定义列表
mylist = ['x', 'j', 'g']
print mylist

#改变列表
mylist[1] = 'o'
print mylist

#删除元素
del mylist[0]
print mylist

#追加元素
mylist.append('y')
print mylist

#统计某个元素的出现次数
print 'count g is ', mylist.count('g')

#索引位置
print 'index of g is ', mylist.index('g')

#插入元素
mylist.insert(2, '1993')
print mylist

#排序
mylist.sort()
print mylist

#反转
mylist.reverse()
print mylist

print '---------- list end ----------\n'

print '---------- tuple start ----------'

#定义
mytuple = ('h', 'e', 'l', 'l', 'o')
print mytuple

print '---------- tuple end ----------\n'

print '---------- dict start ----------'

#定义
mydict = {'name' : 'xujianguo', 'age' : 21}
print mydict

#根据key获取alue
print mydict['name'] 

print '---------- dict end ----------\n'
