# 写一个函数找出一个整数数组中，第二大的数
# list = [2,4,6,7,4,4,3,25,3]
# list.sort()    # 默认是升序排列
# print(list[-2])

# =======================================

# 加 global
# def my_global():
#     global x
#     x = 8
#
#
# my_global()
# print(x)

# =======================================

# res = filter(lambda x: x % 2 ==1 , [1,2,3,4,5,6,7,8,9,10])
# print(type(res))
# list = []
# for i in res:
#     list.append(i)
# res = list
# print(res)

# ========================================

# x = [i for i in range(10)]
# print(x)

# x = [i**2 for i in range(10) if i%2==1]
# print(x)

# ========================================
# 反转一个整数，例如 -123 ====>  -321
# num = int(input('请输入一个整数:'))
# # l = []
# # for i in str(num):
# #     l.append(i)
# # if l[0]=='-':
# #     ls = l[1:]
# #     ls = ls[::-1]
# #     s = int('-'+''.join(ls))
# # else:
# #     ls = l[::-1]
# #     s = int(''.join(ls))
# # print(s)

# ===========================================
# 一行代码实现1-100之和
# s = sum ([i for i in range(101)])
# print(s)
# ===========================================

# l = [1,2,3,1,2,3,1,5,2,3]
# l = list(set(l))
# print(l)

# ls = []
# for i in l:
#     if i not in ls:
#         ls.append(i)
# l = ls
# print(l)

# ==============================================
# print(sum([1 + 2 + 3 + 10248]))

# 求出列表的所有奇数并构造新列表
# l = [1,23,12,2,4,3,5,4,5,7,6,7,68,2]
# li = []
# for i in l:
#     if i %2 ==1:
#         li.append(i)
# l = li
# print(l)


# l = [1,2,2,3,4,4,5,7]
# ls = []
# for i in l:
#     if i % 2 ==1:
#         ls.append(i)
# l = ls
# print(l)
# print(l.index(2))
# l.remove(2)
# print(l)

# import numpy as np
# s = np.arange(10,step=2)
# print(s)

# print(ord('9')-ord('0'))
# def atoi(s):
#     num = 0
#     for v in s:
#         num = num * 10 + ord(v) - ord('0')
#     return num
#
# print(atoi('123'))


# 单例

# class A(object):
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#         return cls._instance
# s = A()
# c = A()
# print(id(s))
# print(id(c))

# 冒泡排序
# list = [1,2,4,5,2,6,354,32,2,212,564,24,434,454,45,77,232]
#
# for i in range(len(list)):
#     for j in range(0,len(list) - i - 1):
#         if list[j] > list[j + 1]:
#             list[j], list[j + 1] = list[j + 1], list[j]
# print(list)

# def ssss(cls):
#     instance = {}
#     def wrapper(*args,**kwargs):
#         if cls not in instance:
#             instance[cls] = cls(*args,**kwargs)
#         return instance[cls]
#     return wrapper
#
# @ssss
# class foo(object):
#     pass
#
# s = foo()
# l = foo()
#
# print(id(s))
# print(id(l))


##################################################
# 装饰器  查看程序运行时间
# import time
# def time_(fun):
#     def wrapper():
#         start = time.clock()
#         fun()
#         end = time.clock()
#         print(end-start)
#     return wrapper
#
# @time_
# def fun():
#     print('hello word')
#
# fun()

###########################################
# 斐波那契数列
# 1 1 2 3 5 8 13 21 34 55

# a = 1
# b = 1
# n = 10
# for i in range(10):
#     if i <=1:
#         m = 1
#     else:
#         a,b = b,a+b
#         m = b
# print(m)

# 单例

# class A(object):
#     _instance= None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#             return cls._instance
#         return cls._instance
# s = A()
# x = A()
# print(id(s))
# print(id(x))


# def xxx(cls):
#     instance = {}
#     def wrapper(*args,**kwargs):
#         if cls not in instance:
#             instance[cls]=cls(*args,**kwargs)
#         return instance[cls]
#     return wrapper
#
# @xxx
# class S(object):
#     pass
# a = S()
# b = S()
# print(id(a))
# print(id(b))

# 装饰器写一个程序运行时间的函数
# import time
# def tt(fun):
#     def wrapper():
#         start = time.clock()
#         fun()
#         end = time.clock()
#         print(end-start)
#     return wrapper
# @tt
# def fun():
#     print('hello world')
# fun()

# 冒泡排序
# l = [4, 3, 2, 3, 45, 6, 4, 3, 2, 3, 43, 22, 1, 12, 34, 56, 44]
# for i in range(len(l)):
#     for j in range(len(l) - i - 1):
#         if l[j] > l[j + 1]:
#             l[j], l[j + 1] = l[j + 1], l[j]
# print(l)

# 斐波那契数列
# l = []
# n = int(input('请输入长度:'))
# for i in range(n):
#     if i <= 1:
#         l.append(1)
#     else:
#         l.append(l[i-2]+l[i-1])
# print(l)

# def new_fun(fun):
#     def wrapper(username,password):
#         if username=='root' and password=='123456':
#             print('密码正确')
#             print('函数开始执行')
#             return fun()
#         else:
#             print('密码验证失败')
#             return
#     return wrapper
#
# @new_fun
# def login():
#     print('登录成功')
#
# login('root','123456')

# s = '123456'
#
# print(s[::-1])

#
# import datetime
#
# yest_datetime = datetime.datetime.now()-datetime.timedelta(days=1)
# yest_str = datetime.datetime.strftime(yest_datetime, '%Y-%m-%d %H:%M:%S')
# print(yest_str)


# a = [1,2,3,4,5,6,7]
# b = [1,2,3,4,5]
#
# print(a + b)

# import random
#
# s = random.randint(1,10)
# print(s)

# b1=[1,2,3]
# b2=[2,3,4]
#
# print(b1+b2)

# l=[1,1,2,3,4,5,4]
# l = list(set(l))
# print(l)

# b1 = [1,2,3]
# b2 = [2,3,4]
# b1 = set(b1)
# b2 = set(b2)
# print(b1 & b2)


# l = [1,2,3,5,2,3,4,6,8,4,2,1,5]
#
# print(sorted(l))

# result = []
# for x in range(10):
#     result.append(x**2)
# print(result)

# result = [x**2 for x in range(10)]
# print(result)

# seq = [1,2,3,4]
#
# print(id(seq[:]) == id(seq))

# x=0.5
# while x <= 1.0:
#     print(x)
#     x+=0.1

# def fun():
#     for i in range(0,10,2):
#         yield i
#
# for i in fun():
#     print(i)


# gen =  (i for i in range(10))
#
# print(next(gen))

# ===============================
# 斐波那契递归
# class Fib:
#     def __init__(self,max_value):
#         self.prev = 0
#         self.curr = 1
#         self.max_value = max_value
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.curr < self.max_value:
#             res = self.curr
#             self.prev,self.curr = self.curr,self.curr+self.prev
#             return res
#
#         else:
#             raise StopIteration()


print(3*1+3*2+3*3+3*4+3*5)
