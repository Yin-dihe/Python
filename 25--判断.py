# ---01.startswith() 检查字符串是否以指定子串开头，是则返回True 否
"""
mystr = "hello world and itcast and itheima and Python"
print(mystr.startswith('hello'))  # True
print(mystr.startswith('hel'))  # True
print(mystr.startswith('hels'))  # False
"""

#---02.endswith()  检查字符串是否以指定子串结尾，是则返回True 否
"""
mystr = "hello world and itcast and itheima and Python"
print(mystr.endswith('Python'))  # True
print(mystr.endswith('Pythons'))  # False
"""

# ---03.isalpha()  字符串中有一个字符 或者全为字母  则返回True 否则  返回False
"""
mystr = "hello world and itcast and itheima and Python"
print(mystr.isalpha())  # False  因为字符串中包含空格  都为字母才返回True
"""


# ---04.isdigit()  都为数字则返回True
"""
mystr = "hello world and itcast and itheima and Python"
print(mystr.isdigit())  # False  因为字符串中不包含数字
mystr1 = "12345"
print(mystr1.isdigit())  # True  因为字符串中包含数字
"""

# ---05.isalnum()  字符串为  都是数字或都是字母或是数字与字母的组合  则返回True
"""

mystr = "hello world and itcast and itheima and Python"
print(mystr.isalnum())  # False  因为字符串中包含空格
mystr1 = "hello"
print(mystr1.isalnum())  # True
mystr2 = "hello123"
print(mystr2.isalnum())  # True  

"""

# ---06.isspace()  都是空白返回True
"""
mystr = '    '
print(mystr.isspace())  # True
mystr1 = '  1  '
print(mystr1.isspace())  # False
"""
















