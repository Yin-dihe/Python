"""
1.按照经验将不同的变量存储不同的类型的数据
2.验证这些数据到底是什么类型——检测数据类型——type（数据）

"""

num1 = 1
num2 = 1.1
# int--整型
print(type(num1))
# float--浮点型
print(type(num2))
# str--字符串
a = 'hello world'
print(type(a))
# bool--布尔型，通常判断时使用，布尔型有两个取值，True 和 False
b = True
print(type(b))
# list--列表
c = [10, 20, 30]
print(type(c))
# tuple--元组
d = (10, 20, 30)
print(type(d))
# set--集合
e = {10, 20, 30}
print(type(e))
# dict--字典
f = {'name': 'TOM', 'age': 18}
print(type(f))

