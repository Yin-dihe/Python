# 01.index() 返回指定数据的下标位置
# print(name_list.index('TOM'))
"""
name_list = ['TOM', 'Lily', 'ROSE']
print(name_list.index('TOM'))  # 0
"""

# ---02 count()  统计指定数据出现的次数
"""
name_list = ['TOM', 'Lily', 'ROSE']
print(name_list.count('TOM'))  # 1
print(name_list.count('TOMs'))  # 0
"""

# --03 len()  返回列表中的字符个数
# print(len(name_list))  # 3

# --04.in.  not in.判断指定数据是否在某个列表序列，如果在返回True  不在返回False
"""
# 0401.in
name_list = ['TOM', 'Lily', 'ROSE']
print('TOM' in name_list)   # Ture
print('TOMs' in name_list)  # False
# 0402.not in
print('TOM' not in name_list)   # False
print('TOMs' not in name_list)   # Ture
"""
# --05.体验案例
# 需求：注册邮箱，用户输入一个账号名，判断这个账号是否存在，如果存在，提示用户，否则提示用户可以注册
"""
1.请输入您的账号
2.判断if...else
"""
name_list = ['TOM', 'Lily', 'ROSE']
name = input('请输入您的账号：')
if name in name_list:
    print(f'您输入的名字是{name}, 此用户名已经存在')
else:
    print(f'您输入的名字是{name}, 可以注册')





