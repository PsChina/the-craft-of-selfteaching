# coding=UTF-8
# day1
# import random
# r = random.randrange(1, 1000)
# # 布尔运算
# print( 1 == 2 )
# print( 1 != 2 )

# # 流程控制
# if(r%2 == 0):
#     print(r, 'is even.')
# else:
#     print(r, 'is odd.')

# for i in range(10):
#     if i%2 ==1:
#         print(i)

# print('\n')

# for n in range(2, 100):
#     for i in range(2, n):
#         if n%i == 0:
#             break
#     else:
#         print(n)

# # 所谓算法
# for n in range(2,100):
#     for i in range(2, int(n**0.5)+1):
#         if n%i == 0:
#             break
#     else:
#         print(n)

# # 所谓函数
# a = abs(-3.1415926)
# print(a)
# def is_prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     else:
#         return True

# for i in range(80,100):
#     if is_prime(i):
#         print(i)
# # 细节补充

# # day2

# # 值及其相应的运算

# # 值

# #在 Python 中每个函数都有返回值，即便你在定义一个函数的时候没有设定返回值，它也会加上默认的返回值 None……（请注意 None 的大小写！）

# #在不得不对不同类型的值进行运算之前，总是要事先做 Type Casting（类型转换）

# #type()，可以用来查看某个值属于什么类型：

# print( 
#         type(1), 
#         type('1'), 
#         type(1.0), 
#         type([1,2,3]), 
#         type((1,2,3)), 
#         type({1,2,3}),
#         type({'a':'a','b':1,'c':True}),
#         type(False),
#         type(range(10)) # list ?
#     )

# # (<type 'int'>, <type 'str'>, <type 'float'>, <type 'list'>, <type 'tuple'>, <type 'set'>, <type 'dict'>, <type 'bool'>, <type 'list'>)

# # 操作符 end 2019 4 11 12:36





