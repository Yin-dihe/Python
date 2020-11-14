"""
for 临时变量 in 序列:
    重复执行的代码1
    重复执行的代码2
    ....


1.准备一个数据序列
2.for

str1 = 'itheima'
for i in str1:
    print(i)
"""

#  ---01break退出循环

"""
str1 = 'itheima'
for i in str1:
    if i == 'e':
        break
    print(i)
    
"""
# ---02continue退出循环
"""
str1 = 'itheima'
for i in str1:
    if i == 'e':
        continue
    print(i)

"""
# ---03 for...else
"""
语法
for 临时变量 in 序列:
    重复执行的代码1
    .......
else:
    循环正常结束之后要执行的代码
    
    
str1 = 'itheima'
for i in str1:
    print(i)
else:
    print('循环正常结束执行的代码')

"""
#  ---04退出循环  与while语句相同
"""

---0401  break
str1 = 'itheima'
for i in str1:
    if i == 'e':
        break
    print(i)
else:
    print('循环正常结束执行的代码')
    

---0402  continue
str1 = 'itheima'
for i in str1:
    if i == 'e':
        continue
    print(i)
else:
    print('循环正常结束执行的代码')
    
    
"""








