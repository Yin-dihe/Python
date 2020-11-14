# 分析：年龄大于等于18，输出：已经成年，可以上网--准备年龄的数据 和18作比较
# age = 20
# if age >= 18:
#    print('已经成年，可以上网')
# 进阶 input接受用户输入的字符串类型，条件是age和整型18做判断，所以这里要int转换数据类型
"""
1.用户输入
2.保存用户输入的年龄
3.if
****  注意一个点  input 接受的数据类型为str  而18为int型  因此与需要将数据类型进行转换
"""
"""
err:age1为字符串类型  而18为int类型  故需要类型转换
age1 = input('请输入你的年龄：')
if age1 >= 18:
    print('已经成年，可以上网')


age1 = int(input('请输入你的年龄：'))
if age1 >= 18:
    print(f'您的年龄是{age1},已经成年，可以上网')
else:
    print(f'您的年龄是{age1},未成年，不可以上网')
    
    
"""
# 01多重判断


"""


age = int(input('请输入年龄:'))
if age < 18:
    print(f'您的年龄是{age},未成年，不合法')
# elif (age >= 18) and (age <= 60):
elif 18 <= age <= 60:
    print(f'您的年龄是{age},成年，合法')
elif age > 60:
    print(f'您的年龄是{age},退休，不合法')
    
    
"""

#  02if嵌套 坐公交

"""
坐公交，有钱可以上车，没钱不能上车，上车有空座，可以坐，没有空座，只能站

"""
money = int(input('请输入您的余额：'))
if money >= 2:
    print(f'您的余额为{money},可以上车')
    seat = int(input('请输入空座数目：'))
    if seat > 0:
        print('可以坐')
    else:
        print('不可以坐')
elif money <= 2:
    print(f'您的余额为{money},不能上车')








