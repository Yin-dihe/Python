# ---01 一共吃5个苹果  吃完第一个  吃第二个
"""
case 1 吃完第三个吃饱了  第4 第5 不吃    break

i = 1
while i <= 5:
    if i > 3:
        print('吃饱了')
        break
    print(f'吃第{i}个苹果')
    i = i + 1


case 2（重点） 吃的过程中  吃到第三个有虫  继续吃第四个 第五个  continue

i = 1
while i <= 5:
    if i == 3:
        print('不吃了')
        #  如果使用continue 在continue之前一定要修改计数器，否则将进入死循环
        i = i + 1
        continue
    print(f'吃第{i}个苹果')
    i = i + 1
"""

#  --02 while循环嵌套
"""
while 条件1：
     条件1成立执行的代码
     .....
     while 条件2：
         条件2成立执行的代码
         .......
         
j = 1
while j <= 2:
    i = 1
    while i <= 3:
        print('媳妇，我错了')
        i = i + 1
    print('我刷碗')
    j = j + 1
    
"""

# ---0201 while  else
"""
1.书写道歉循环
2.循环正常结束要执行的代码--else

语法
while 条件：
      条件成立重复执行的代码
else:
       循环正常结束之后要执行的代码

"""
#  ---0202退出循环的方式  break对后面的语句影响  后面的else语句不会执行
"""
i = 1
while i <= 5:
    if i == 3:
        print('不真诚')
        break
    print('媳妇，我错了')
    i = i + 1
else:
    print('被原谅，真开心')
"""

#  ---0202退出循环的方式  cuntinue要记得修改计数器，执行continue后  后面的语句正常执行
"""
i = 1
while i <= 5:
    if i == 3:
        print('不真诚')
         i = i + 1
        continue
    print('媳妇，我错了')
    i = i + 1
else:
    print('被原谅，真开心')
"""
i = 1
while i <= 5:
    if i == 3:
        print('不真诚')
        i = i + 1
        continue
    print('媳妇，我错了')
    i = i + 1
else:
    print('被原谅，真开心')




# ---03打印星号（正方形）
"""
1.打印一个*
2.打印一行5个
print('*', end='')  取消回车换行
3. 打印5行*  循环5行
  print()   换行 print 默认回车
  
j = 0
while j < 5:
    i = 0
    while i < 5:
        print('*', end='')
        i = i + 1
    print()
    j = j + 1

"""

# ---04打印星号（三角形）
"""
j = 0
while j <= 5:
    i = 0
    while i < j:
        print('*', end='')
        i += 1
    print()
    j += 1

"""

# ---05打印乘法表
"""

1.打印一个乘法表达式 x * x =x*x
2.一行打印多个表达式--一行表达式的个数和行号数相等--循环
3.打印多行表达式的个数和行号数相等
注意   格式 print(f'{i}*{j}={s}  ', end='\t')


j = 1
while j <= 9:
    i = 1
    while i <= j:
        s = i * j
        print(f'{i}*{j}={s}', end='\t')
        i += 1
    print()
    j += 1

"""





