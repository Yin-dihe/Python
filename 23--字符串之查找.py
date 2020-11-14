# find
# ---01.find()
#  语法：字符串序列.find(字串,开始位置下标，结束位置下标)

"""
mystr = "hello world and itcast and itheima and Python"
print(mystr.find('and'))  # 12
print(mystr.find('and', 15, 30))  # 23
print(mystr.find('ands'))  # ands字串不存在  返回值为-1
# ---02index()查找
print(mystr.index('and', 15, 30))  # 23
# print(mystr.index('ands'))  # ands字串不存在  index查找的字符串不存在则报错

# ---03count()查找  统计次数
print(mystr.count('and', 15, 30))  # 1
print(mystr.count('and'))  # 3
print(mystr.count('ands'))  # ands字串不存在  返回值为0

# ---04rfind()
print(mystr.rfind('and'))  # 35  从字符串右侧开始寻找
# --05rindex()
print(mystr.rindex('and'))  # 35  从右侧开始查找
print(mystr.rindex('ands'))  # 字符串不存在  报错

"""








