
"""
str1 = 'abcdefg'
# 得到整个字符
print(str1)
# 下标得到的是下标为某个数字的数据
print(str1[2])

"""

# ---01得到abc 这3个数据怎么操作

"""
#  方法  切片
序列[开始位置下标：结束位置下标：步长]  左闭右开区间
注意：
1.不包含结束位置下标对应的数据，正负整数均可
2.步长是选取的间隔，正负整数均可，默认步长为1

"""

str1 = '012345678'
print(str1[2:5:1])
print(str1[2:5:2])
print(str1[2:5])  # 234  默认步长为1
print(str1[:5])  # 01234  未写开始位置  默认从0开始选取
print(str1[2:])  # 2345678  未写结束位置  默认从开始位置选取到完
print(str1[:])  # 012345678  未写开始结束位置  输出所有

# 步长为负数测试
print(str1[::-1])  # 876543210  如果步长为负数，表示倒叙选取
print(str1[-4:-1])  # 567  从后向前类推  -1表示最后一个
# 终极测试  重点  如果选取方向(下标开始到结束的方向)和步长的方向冲突，则无法选取数据
print(str1[-4:-1:-1])  # 未选取出数据，从-4开始到-1结束，选取方向为从左到右，但是步长-1
print(str1[-1:-4:-1])
print(str1[6:9:1])


