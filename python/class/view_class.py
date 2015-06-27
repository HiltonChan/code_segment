#!/usr/bin/env python
#-*- coding:utf8 -*-

"""
    类：
        函数跟方法的区别：
            1.方法是将第一个参数绑定到所属的实例上，指的就是self，如showMessage
            2.函数只是简单的函数定义和使用，没有绑定这个特征

        类的命名空间：
            所有位于class语句中的代码都在特殊的命名空间中执行，这个命令空间可有类的所有成员访问

        多重继承：
            1.一个类可以拥有多个父类的方法
            2.对于父类中有相同名字的方法，前面的父类方法会覆盖后面的父类方法

        魔法方法：
            具体指不需要我们明显调用，python会暗中调用的方法

            __init__:
                类别：构造方法
                特点：
                    会在类被创建的时候调用

            __del__:
                类别：析构方法
                特点：
                     类被回收的时候调用

        静态方法和类方法：
            1.静态方法和类方法分别在创建时候分别被装入staticmethod类型喝classmethod类型的对象中
            2.静态方法的定义没有self参数，能够被类本身直接调用，类方法是绑定方法
"""

class Person:
    name = "xujianguo"
    age = 22

    def __init__(self):
        print 'person class init'

    def showMessage(self):
        print 'name : ', self.name
        print 'age : ', self.age

    def changeAge(self):
        self.age += 1

    def __del__(self):
        print 'person class destroy'

    @staticmethod
    def printStatic():
        print 'Person Static Method'

def test():
    print 'test method'

class A:
    def a(self):
        print 'a'

    def show(self):
        print 'A show'

class B:
    def b(self):
        print 'b'

    def show(self):
        print 'B show'

class C(A, B):
    pass

person = Person()
person.showMessage()
test()

person1 = Person()
person1.changeAge()
print person1.age
person2 = Person()
print person2.age

c = C()
c.a()
c.b()
c.show()

Person.printStatic()
