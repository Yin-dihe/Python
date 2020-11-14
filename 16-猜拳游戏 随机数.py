"""
1.出拳
玩家  手动出拳
电脑  随机出拳（先固定出拳，再随机出拳）
2. 判断输赢
  2.1 玩家获胜
  2.2 平局
  2.3 电脑获胜
"""
#  ---01电脑固定出拳

"""
# 1.出拳
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布：'))
# 电脑
computer = 1
#  2.判断输赢
if((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
"""

#  ---02随机数
"""
1.导出random模块
import 模块名
2.使用random模块中的随机整数功能
random.randint(开始，结束)  包含开始与结束的数字

import random
num = random.randint(0, 2)
print(num)
"""
#   ---03电脑随机出拳

"""
# 1.出拳
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布：'))
# 电脑
import random
computer = random.randint(0, 2)
print(f'电脑是{computer}')
#  2.判断输赢
if((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
    
"""


#  ---04三目运算符
"""
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式

"""
a = 1
b = 2
c = a if a > b else b
print(c)

#  需求： 两个变量：比较大小  如果变量1大于变量2  执行变量1-变量2 否则  变量2-变量1

aa = 10
bb = 50
cc = aa - bb if aa > bb else bb - aa
print(cc)











