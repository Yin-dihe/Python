a = 0
b = 2
c = 0
print((a==b))
# 1.and 同真则真
print(a > b and c > b)
print((a > b) and (c > b))

# 2.or 或 有真则真   同假则假
print((a > b) or (c > b))
# 3.not 非  取反
print(not False)

#  数字之间的逻辑运算
# and运算符 只要有一个值为0，则结果为0  否则结果为最后一个非0数字
print(a and b)
print(c and b)
# or运算符  只要所有值为0结果才为0，否则结果为第一个非0数字

print(a or b)
print(a or c)


