#  ---01while的语法
"""
while 条件：
    条件成立执行的代码1
    条件成立执行的代码2
    ........

"""
#  --02需求  重复打印5次  我最棒 -- 1， 2， 3， 4，5， --数据表示循环的次数--第一次是1，最后一次为5
"""
i = 1
while i <= 5:
    print('我最棒')
    i = i + 1
"""


# ---03需求  计算1-100累加
"""
1.准备数据 增量为1
2.准备变量保存运算得结果
3.循环做加法运算
4.打印结果
5.验证结果正确性

#  1.准备数据
i = 1
# 结果变量
sum = 0
# 循环
while i <= 3:
    #  加法运算  前两个数得结果加第三个数
    sum = sum + i
    i = i + 1
print(f'总和为{sum}')

"""
# ---04  计算1-100偶数之和
"""
1.准备累加的数字  开始1 结束100 增量1
2. 准备 保存结果的变量sum
3. 循环加法运算--如果偶数才加法运算  和2取余数为0
4.输出结果
5.验证结果

#  ---0401 条件判断和对2取余
i = 2
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
print(sum)

#  ---0402 计数器法
i = 2
sum = 0
while i <= 100:
    sum = sum + i
    i = i + 1
print(sum)
"""



