# replace()
"""
# 语法
字符串序列.replace(旧子串,新子串，替换次数)

"""
# ---01replace()把and换成he  replace函数有返回值，返回值是修改后的答案
"""
mystr = "hello world and itcast and itheima and Python"
new_str = mystr.replace('and', 'he')
new_str = mystr.replace('and', 'he', 1)  # hello world he itcast and itheima and Python
new_str = mystr.replace('and', 'he', 10)  # 替换个数超出原有的个数  则将所有的都替换掉
print(mystr)  # hello world and itcast and itheima and Python
print(new_str)  # hello world he itcast he itheima he Python

# ***调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# ---说明 字符串是不可变数据类型
# 数据是否可以改变划分为 可变数据 和 不可变数据
"""

# ---02split() --分割，返回一个列表，丢失分割字符
"""
语法：
字符串序列.split(分割字符, num)   num表示分割字符出现的次数，即将返回数据个数为num+1个

mystr = "hello world and itcast and itheima and Python"
list1 = mystr.split('and')
list1 = mystr.split('and', 2)
print(list1)
"""

# ---03.join()--合并列表里的字符串数据为一个大字符串
"""
语法：
字符或子串.join(多字符串组成的序列)

mylist = ['aa', 'bb', 'cc']
new_str = '***'.join(mylist)
print(new_str)  # aa***bb***cc
"""

# ---04.capitalize() 将字符串的首字母转换为大写
"""
mystr = "hello world and itcast and itheima and Python"
new_str = mystr.capitalize()
print(new_str)  # Hello world and itcast and itheima and python
"""
# ---05.title()  将字符串中每个字符的首字母进行大写转换
"""
mystr = "hello world and itcast and itheima and Python"
new_str = mystr.title()
print(new_str)  # Hello World And Itcast And Itheima And Python
"""
# ---06.upper()  将字符串中每个字符进行大写转换
"""
mystr = "hello world and itcast and itheima and Python"
new_str = mystr.upper()
print(new_str)  # HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON
"""
# ---06.lower()  将字符串中每个字符进行小写转换
"""
mystr = "hello world and itcast and itheima and Python"
new_str = mystr.upper()
print(new_str)  # hello world and itcast and itheima and python
"""

# ---07.lstrip() 删除字符串左侧空白字符
"""
mystr = "  hello world and itcast and itheima and Python  "
print(mystr) #   hello world and itcast and itheima and Python
new_str = mystr.lstrip()
print(new_str)  # hello world and itcast and itheima and Python  
"""
# ---08.rstrip() 删除字符串右侧空白字符
"""
mystr = "  hello world and itcast and itheima and Python  "
print(mystr) #   hello world and itcast and itheima and Python
new_str = mystr.rstrip()
print(new_str)  #   hello world and itcast and itheima and Python
"""
# ---09.strip() 删除字符串两侧空白字符
"""
mystr = "  hello world and itcast and itheima and Python  "
print(mystr) #   hello world and itcast and itheima and Python
new_str = mystr.strip()
print(new_str)  # hello world and itcast and itheima and Python
"""

# ---10.ljust() 返回一个原字符串左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串
"""
语法：
字符串序列.ljust(长度， 填充字符)

mystr = "hello"
print(mystr)  # hello
new_mystr = mystr.ljust(10)  
print(new_mystr)  # hello     
new_mystr1 = mystr.ljust(10, '*')
print(new_mystr1)  # hello*****
"""
# ---11.rjust() 返回一个原字符串右对齐，并使用指定字符（默认空格）填充至对应长度的新字符串
"""
语法：
字符串序列.rjust(长度， 填充字符)
mystr = "hello"
print(mystr)  # hello
new_mystr = mystr.rjust(10)  
print(new_mystr)  #      hello
new_mystr1 = mystr.rjust(10, '*')
print(new_mystr1)  # *****hello
"""
# ---12.center() 返回一个原字符串右对齐，并使用指定字符（默认空格）填充至对应长度的新字符串
"""
语法：
字符串序列.center(长度， 填充字符)
mystr = "hello"
print(mystr)  # hello
new_mystr = mystr.center(10)
print(new_mystr)  #   hello   
new_mystr1 = mystr.center(10, '*')
print(new_mystr1)  # **hello***
"""


