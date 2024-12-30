# #print("hello")
# #字符串：需要加上双引号
# print (666)
# print(13.14)
# print("zxhzgy")
# """
# 变量：程序运行时，记录数据
# 变量名称=变量的值
# """
#
# """
# rest_money=12
# print("钱包还有：",rest_money)
#
# rest_money=rest_money-10
# print("买了面包钱包还有：",rest_money)
#
# money= 50
# print("当前钱包余额： ",money,"元")
# ice=10
# print("买了冰淇淋，花费：",ice,"元")
#
# coke=5
# print("买了可乐，花费：",coke,"元")
# money =money-ice-coke
# print("最终，钱包剩余：",money,"元")
# """
#
# """
# type(被查看类型的数据)
# 变量没有类型，存储的数据有类型
# """
# # 使用直接输出数据类型
# print(type(666))
#
# # 用变量存储type()语句结果
#
# type_string=type("黑马程序员工")
# print(type_string)
#
# # 使用type（）语句，查看变量中存储的数据类型信息
# name="黑马程序员"
# name_type=type(name)
# print(name_type)
#
# """
# #将数字类型转换为字符串
# """
# num_str=str(11)
# print(type(num_str),num_str)
#
# # 将字符串转换成数字
# num=int("11")
# print(type(num),num)
# """
# int(x)
# float(x)
# str(x)
# 把x的类型转换为int,float,str
# 标识符：在编程时所使用的一系列名字，用于给变量、类、方法等命名
# 标识符命名规则：（中英文，数字，下划线）；大小写敏感，不可用关键字，数字开头
# 变量命名规范:见名知意；多个单词组合用下划线分隔，英文字母全小写
#
# 运算符
# +-*/加减乘除
# 取整除//
# %取余
# **指数
# """
#
#
# """
# 字符串3种定义法
# 1：单引号
# 2：双引号
# 3.三引号
# 在字符串内包含引号
#
# """
# name='lily'
# name1="cici"
# name2="""xiaoguai """
# name4='"nihao"'
# name5="'kaixin'"
# #用转义字符\解除引号效用（\后面的引号解除效用）
#
# name6="\'nihao\'"
# print(name6)
#
# #字符串拼接用%s占位字符串，%d整数，%f浮点数
# name7="小乖"
# age=2
# print("小猫的名字是： %s,小猫的年龄是：%d" %(name7,age))
#
# #字符串格式化，精度控制
# num1=11
# num2=11.345
# print("数字11宽度限制5，结果是：%5d" % num1)
# print("数字11宽度限制1，结果是:%1d" % num1)
# print("数字11.345宽度限制7,小数精度2，结果是：%7.2f" % num2)
# print("数字11宽度限制无，小数精度2，结果是：%.2f" % num2)
#
# #字符串格式化——快速写法 ： f"内容{变量}" 不限制数据类型，不做精度控制
# print(f"小猫的名字是：{name7},小猫的年龄是{age}")
# """
# 对表达式进行格式化：
# 表达式：一条具有明确结果的代码语句 如：1+1，5*2
# """
# print("1*1 的结果是： %d" %(1*1))
# print(f"1*5的结果是： {1*5}" )
# print("字符串在python中的类型名是：%s "%type("字符串"))
#
# name="传智播客"
# stock_price=19.99
# stock_code= "003032"
# stock_price_daily_growth_factor=1.2
# growth_days=7
# print(f"公司：{name},股票代码：{stock_code}, 当前股价：{stock_price}")
# print("每日增长系数是：%.2f" % stock_price_daily_growth_factor,
#       "经过%d次的增长后，"% growth_days,
#       "股价达到了：%.2f" %(stock_price*stock_price_daily_growth_factor**7))

"""
演示python的input的语句
获取键盘的输入信息
input（提示信息）
"""
from itertools import count
from operator import index

from webcolors import names

#print("你是谁")
# name=input("你是谁")
# print("我知道了，你是：%s" % name )
#
# """
# 输入数字类型
# """
# num=input("你的银行卡密码是")
# num=int(num)
# print("你的银行卡密码的类型是：",type(num))
# user_name=input("您好：")
# user_type=input("您是尊贵的：")
# print("您好：",user_name,"您是尊贵的：",user_type,"用户，欢迎您的光临。")
"""
布尔类型
"""
# bool_1=True
# bool_2=False
# print(f"bool_1变量的内容是：{bool_1}，类型是{type(bool_1)}")
# print(f"bool_2变量的内容是：{bool_2}，类型是{type(bool_2)}")
# # if 判断语句
# age=30
# if age>18:
#     print("我已经成年了")
# print("时间过得真快")
#
# print(f"欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
# age=input("请输入你的年龄：")
# age=int(age)#age=int(input("请输入你的年龄："))
# if age>18:
#     print("您已成年，游玩需补票10元。")
# print("祝您游玩愉快。")
# print("欢迎来到黑马动物园。")
# tall=int(input("请输入你的身高（cm）："))
# if tall>120:
#     print("您的身高超过120cm，游玩需要购票10元。")
# else:
#     print("您的身高未超出120cm，可以免费游玩")
# print("祝您游玩愉快")
# num=5
# if int(input("请输入猜想的数字：")) == num:
#     print("第一次就猜对了")
# elif int(input("猜错了，再猜一次：")) ==num:
#     print("猜对了")
# elif int(input("猜错了，再猜一次："))==num:
#     print("恭喜最后一次，猜对了")
# else:
    #print("Sorry,猜错了")
# import random
# num=random.randint(1,10)
# guess_number=int(input("你猜测的数字："))
# if guess_number == num:
#     print("恭喜第一次猜测成功")
# else:
#     if guess_number>num:
#         print("你猜的数字大了")
#     else:
#         print("你猜的数字小了")
#     guess_number = int(input("再次输入你猜测的数字："))
#     if guess_number == num:
#         print("恭喜第二次猜测成功")
#     else:
#         if guess_number > num:
#             print("你猜的数字大了")
#         else:
#             print("你猜的数字小了")
#         guess_number = int(input("再次输入你猜测的数字："))
#         if guess_number == num:
#             print("恭喜第三次猜测成功")
#         else:
#             print("三次机会用完了")
# i=0
# while i<100:
#     print("小怪，你好奇怪")
#     i +=1

# sum_num=0
# i=1
# while i<=100:
#     sum_num=i+sum_num
#     i=i+1
# print(sum_num)
# import random
# num=random.randint(1,100)
# count=0
# flag=True
# while flag:
#     guess_num=int(input("请输入你猜测的数字： "))
#     count +=1
#     if guess_num==num:
#         print("猜中了")
#         flag=False
#     else:
#         if guess_num > num:
#             print("猜大了")
#         else:
#             print("猜小了")
# print("你总共猜测了",count ,"次数")
# i=1
# while i<=100:
#     print (f"今天是第{i}天，准备表白")
#
#     j=1
#     while j<10:
#         print(f"送第{j}只玫瑰花")
#         j+=1
#     print(f"小美我喜欢你")
#     i+=1
# print(f"坚持{i-1}天，成功")
"""
print不换行
print("hello",end='')
print("world",end='')
结果是：helloworld
制表符\t
多行字符串进行对齐
print("hello\tworld")
print("itheima\tbest")
结果：
hello	world
itheima	best
"""
# #定义外层循环的控制变量
# i=1
# while i<=9:
#     #定义内层循环的控制变量
#     j=1
#     while j<=i:
#         #内层循环的输出语句，不换行，用\t对齐
#         print(f"{j}*{i}={j*i}\t",end='')
#         j+=1
#     i+=1
#     print()#输出一个空内容就是输出一个换行
"""
for循环就是对待办事项，一个个处理
for 临时变量 in 待处理数据集：
    循环满足条件时执行的代码
待处理数据集被称为：序列类型指内容可以一个个被依次取出（例如：字符串，列表，元组等）
range(5)表取出的数字为[0,1,2,3,4]
range(5,10)表取出的数字为[5,6,7,8,9]
range(5,10,2)表取出的数字为[5,7,9]  (后面的2为数字之间的差值)
"""
# name="xiaoguai"
# for x in name:
#     print(x)
# name="itheima is a brand of itcast"
# count=0
# for x in name:
#     if x =="a":
#         count+=1
# print(f"itheima is a brand of itcast中共含有：{count}个字母a")
# num=100
# count=0
# for i in range(1,num):
#     if i%2 ==0:
#         count+=1
# print(f"1到100（不含100本身）范围内，有{count}个偶数")
# i=0
# for i in range(1,101):
#     print(f"今天是第{i}天")
#     for j in range(1,11):
#         print(f"第{j}朵花")
#     print("我喜欢你")
# print(f"第{i}天，成功")
# j=0
# i=0
# for i in range (1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}\t",end='')
#     print()
"""
continue:中断所在循环的当次执行，直接进入下一次
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")
只会执行语句1，不会执行语句2
continue只有紧挨着continue后面的语句不会执行
break直接结束所在的循环

"""

# money=10000
# for i in range(1,21):
#     import random
#     score = random.randint(1,10)
#
#     if score<5:
#         print(f"员工{i}绩效分{score},不满足，不发工资，下一位")
#         continue
#
#     if money>=1000:
#         money-=1000
#         print(f"员工{i},满足条件放发工资1000，公司账户余额：{money}元")
#     else:
#         print(f"余额不足，当前余额{money}元，不足以发放工资，不发了")
#         break
"""
函数：组织好的，可重复使用的，实现特定功能的代码段
定义：
def 函数名（传入参数）：
    函数体
    return 返回值
函数调用：
函数名（参数）
传入参数：在函数执行时，接受外部（调用）提供的数据
外部调用时的参数为实际参数（实参）；函数定义中的参数为形式参数（形参）
参数之间都用，分隔
返回值：程序中函数完成事情后，最后给调用者的结果
def 函数名（传入参数）：
    函数体
    return 返回值   return 后面的代码不执行了
变量=函数名（参数）  变量能接收函数的返回值

如果没有return 或者 return None 返回值为空
在if中None可以表示false
None还可以声明初始没有意义的变量

函数嵌套调用：在一个函数里面又调用了另外一个函数


变量作用域：变量作用范围
局部变量：在函数体内部的变量只在函数体内生效，函数运行时临时保存数据，函数执行后被销毁
        出了函数体，局部变量无法使用
        
全局变量：在函数体内外都生效
global关键字：在函数内部声明变量为全局变量

"""
# str1="xiaoguai"
# def my_len(data):
#     count=0
#     for i in data:
#         count+=1
#     print(f"字符串{data}长度为{count}")
# my_len(str1)
# def text():
#     print("欢迎来到黑马程序员！\n请你出示健康码以及72小时核算证明")
#
# text()
# def add(x,y):
#     result=x+y
#     print(f"{x}+{y}的计算结果是：{result}")
# add(4,5)
# def check_degree(temp):
#     if temp<37.3:
#         print(f"欢迎来到黑马程序员！请出示你的健康码以及72小时核算证明，并配合测量体温\n体温测量中，您的体温是{temp}度，体温正常请进")
#     else:
#         print(
#             f"欢迎来到黑马程序员！请出示你的健康码以及72小时核算证明，并配合测量体温\n体温测量中，您的体温是{temp}度，需要隔离")
# check_degree(39)
# def add(a,b):
#     result=a+b
#     return result
# r=add(5,6)
# print(r)
"""
函数的说明文档
"""
# def add(x,y):
#     """
#     add返回两数相加结果
#     :param x:相加的其中一个数
#     :param y:另外一个数字
#     :return:相加结果
#     """
#     result=x+y
#     print(f"2数相加的结果是：{result}")
#     return result
# def func_b():
#     print(f"xiaoguai")
# def func_a():
#     print(f"1")
#     func_b()
#     print(f"2")
# func_a()

# def test_a():
#     num=100
#     print(num)
# test_a()


# num=200
# def test_a():
#     print(f"test_a:{num}")
#
# def test_b():
#     global num
#     num=500    #局部变量
#     print(f"test_b:{num}")
#
# test_a()
# test_b()
# print(num)
"""
money=5000000
name=None
name=input("请输出您的姓名：")

def querry(show_header):
    if show_header:
        print(f"------------查询余额--------")
    print(f"{name},您好，您的余额剩余为{money}")

def saving(num):
    global money
    money += num
    print("--------------存款----------")
    print(f"{name},您好,您存款{num}元成功")
    querry(False)

def get_money(num):
    global money
    money-=num
    print("--------------取款----------")
    print(f"{name},您好,您取款{num}元成功")
    querry(False)

def main():
    print("--------------主菜单----------")
    print(f"{name},您好,欢迎来到银行，请选择操作")
    print(f"查询余额\t[输入1]")
    print(f"存款\t\t[输入2]")
    print(f"取款\t\t[输入3]")
    print(f"退出\t\t[输入4]")
    return input("请输入您的选择")


while True:
    keyboard_input=main()
    if keyboard_input=="1":
        querry(True)
        continue
    elif keyboard_input=="2":
        num=int(input("输入您想存的钱"))
        saving(num)
        continue

    elif keyboard_input=="3":
        num = int(input("输入您想取的钱"))
        get_money(num)
        continue
    else:
        print("退出程序")
        break
"""
"""
数据容器：一种可以容纳多份数据的数据类型，容纳的每一份数据为一个元素，每个元素可以是任意类型的数据：字符串、数字、布尔。
5类数据容器：列表list、字典dict、元组tuple、字符串str、集合set

list：列表中每一个数据都是元素；列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套
字面量：[元素1，2，3，4，5]
定义变量：变量名称=[元素1，2，3，4，5]
定义空列表：变量名称=[]；变量名称=list()
列表下标索引
ps:可以反向索引，最后一个为-1，然后依次递减-2，-3


列表的常用操作（方法）
列表提供一系列的功能：插入、删除、清空、修改、统计元素个数。这些功能被称为列表的方法
方法：函数是一个封装的代码单元，可以提供特定的功能，在python中，将函数定义为class的成员
那么函数就会被叫做方法。（将函数放在class里面，函数就会叫做方法）
方法跟函数调用形式不同
列表特点：
可以容纳多个元素（2**63-1）
容纳不同类型
有序，可重复
可以增删改查等

"""
# my_list=["xiaoguai",2,"name_huanglian",True]
# print(my_list)
# print(type(my_list))
#
# my_list=[[3,4,5,6],["xiaoguai","huanglian"]]
# print(my_list)

# my_list=["tom","xiaoguai","age"]
# print(my_list[0])
# print(my_list[-1])
# my_list=[[1,2,3],[4,5,6]]
# print(my_list[1][1])
"""

查询功能：查询指定元素在列表的下标
使用：列表.index（元素）
my_list=["xiaoguai","age"]
index=my_list.index("age")
print(index) 结果为1，说明age在列表中位置是1
"""

"""

修改下标索引值：
列表【下标】=值
my_list=["xiaoguai","age"]
my_list[0]="huanglian"
print(my_list) 结果为：['huanglian', 'age']
"""

"""
插入元素：
列表.insert(下标，元素)在指定的下标位置，插入新的元素ps:这个下标是新元素插入后的位置
my_list=[1,2,3]
my_list.insert(1,'xiaoguai')
print(my_list)   结果为[1, 'xiaoguai', 2, 3]
"""

"""
追加元素
列表.append(元素)，将指定元素，追加到列表的尾部（单个元素）
my_list=[1,2,3]
my_list.append(4)
print(my_list)  结果：[1, 2, 3, 4]

追加一批元素
列表.extend(其他数据容器)
my_list=[1,2,3]
my_list1=["xiaoguai","huanglian"]
my_list.extend(my_list1)
print(my_list)  结果是：[1, 2, 3, 'xiaoguai', 'huanglian']
"""

"""
删除元素
del列表[下标]
my_list=["xiaoguai",2,"age","huanglian"]
del my_list[1]
print(my_list) 结果是['xiaoguai', 'age', 'huanglian']

列表.pop(下标)
my_list=["xiaoguai",2,"age","huanglian"]
element=my_list.pop(0)
print(f"删除元素后新列表：{my_list},删除的元素：{element}") 
结果是：删除元素后新列表：[2, 'age', 'huanglian'],删除的元素：xiaoguai

删除某元素在列表中的第一次出现，只能移除一个元素
列表.remove(元素)
my_list=["xiaoguai",2,"age","huanglian",2,2]
my_list.remove(2)
print(my_list)
结果是：['xiaoguai', 'age', 'huanglian', 2, 2]

"""

"""
清空列表：
列表.clear()
"""

"""
统计某元素在列表中的数量
列表.count(元素)
my_list=[1,1,1,"xiaoguai","huanglian"]
count=my_list.count(1)
print(f"列表中1的数量是：{count}")
结果是：列表中1的数量是：3

统计列表中元素数量
len(列表)
my_list=[1,1,1,"xiaoguai","huanglian"]
count=len(my_list)
print(f"列表中的元素数量是：{count}")
结果是：列表中的元素数量是：5



练习：
student_age=[21,25,21,23,22,20]
student_age.append(31)
print(f"追加的一个学生年龄后列表是{student_age}")
student_age.extend([23,33,30])
print(f"再次追加的3个学生年龄后列表是{student_age}")
student1=student_age[0]
print(f"取出第一个学生的年龄是{student1}")
student2=student_age[-1]
print(f"取出最后一个学生的年龄是{student2}")
index=student_age.index(31)
print(f"取出学生的年龄是31,所在下标为{index}")
"""


"""
用while循环遍历列表中的所有元素
定义一个变量表示下标，从0开始
循环条件为 下标值<列表的元素数量
index=0
while index<len(列表)：
    元素=列表[index]
    对元素进行处理
    index+=1
def list_while_func():
    my_list=["xiaoguai",1,2,"age","huanglian"]
    index=0
    while index<len(my_list):
        element=my_list[index]
        print(f"列表的元素{element}")
        index +=1
list_while_func()
结果：
列表的元素xiaoguai
列表的元素1
列表的元素2
列表的元素age
列表的元素huanglian


用for循环遍历列表
def list_for_func():
    my_list = ["xiaoguai", 1, 2, "age", "huanglian"]
    for i in my_list:
       print(f"列表的元素为:{i}")
list_for_func()

结果是
列表的元素为:xiaoguai
列表的元素为:1
列表的元素为:2
列表的元素为:age
列表的元素为:huanglian

练习：
def for_list():
    my_list=[1,2,3,4,5,6,7,8,9,10]
    my_new_list=[]
    for element in my_list:
        if element%2 == 0:
            my_new_list.append(element)
    print(f"列表中的偶数组成的新列表：{my_new_list}")
for_list()


def while_list():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_new_list = []
    i=0
    while i<len(my_list):
        element=my_list[i]
        if element%2 ==0:
            my_new_list.append(element)
        i +=1
    print(f"列表中的偶数组成的新列表：{my_new_list}")
while_list()
"""


"""
元组
元组可以存储多个不同类型元素，不可修改
元组内如果有list,可以修改list里面的内容
t=(1,2,["xiaoguai","age",2])
print(f"t的内容是：{t}")
t[2][0]="huanglian"
print(f"t的内容是：{t}")
结果是：
t的内容是：(1, 2, ['xiaoguai', 'age', 2])
t的内容是：(1, 2, ['huanglian', 'age', 2])



定义元组变量：变量名称=（元素，元素，元素）
定义空元组：
变量名称=（）
变量名称=tuple（）
定义单个元素的元组在元素后加，否则数据类型会是str

元组可以嵌套
t=((1,2,3),(4,5,6))
print(f"t的类型是{type(t)},内容是{t}")
结果是：
t的类型是<class 'tuple'>,内容是((1, 2, 3), (4, 5, 6))

元组的遍历
while
t=(1,2,3,4,5,6,7)
index=0
while index<len(t):
    print(f"元组的元素有{t[index]}")
    index +=1
元组练习：
student_infor=("周杰伦",11,["footbal","music"])
index=student_infor.index(11)
name=student_infor[0]
student_infor[2].pop(0)
# del student_infor[2][0]
student_infor[2].append("coding")
print(student_infor)
"""

"""
字符串
也不可修改，增删改查
可重复

查找特定字符串的下标索引值：
my_str="xiaoguai age is 2"
print(my_str.index("age"))  结果是：9

字符串替换：
字符串.replace(字符串1，字符串2)
将全部字符串1改为字符串2，得到一个新的字符串

字符串分割：
字符串.split(分隔字符串)
按照指定的分隔字符串，将字符串划分为多个字符串，并存入列表对象中
字符串本身不变，而是得到了一个列表对象
my_str="xiaoguai age is 2"
my_new_str=my_str.split(" ")
print(my_new_str) 结果是['xiaoguai', 'age', 'is', '2']

字符串的规整操作（去前后空格）
字符串.strip()
my_str="  xiaoguai age is 2  "
my_new_str=my_str.strip()
print(my_new_str)
结果是：xiaoguai age is 2

去除前后指定字符串
字符串.strip(字符串)
my_str="12 xiaoguaiage is 211"
my_list=my_str.strip("12")实际去除的是1，2两个字符串
print(my_list)
结果是：
xiaoguaiage is

统计字符串内某字符串出现的次数：
字符串.count(字符串)

统计字符串的数字个数：
len(字符串)

练习：
my_str="itheima itcast boxuegu"
num=my_str.count("it")
print(num)
my_new_str=my_str.replace(" ","|")
print(my_new_str)
my_new2=my_new_str.split("|")
print(my_new2)
"""

"""
数据容器：
序列：内容连续、有序、可使用下标索引的一类数据容器
列表、元组、字符串，均可以为序列
序列操作：
切片：从一个序列中取出来一个子序列
序列[起始下标：结束下标：步长]  不包含结束下标对应的元素
步长为负数倒叙进行

#对list进行切片，1开始，4结束，步长1
my_list=[0,1,2,3,4,5,6]
result1=my_list[1:4]
print(result1)   结果是[1, 2, 3]

#对tuple进行切片，从头开始，到尾结束，步长1
my_tuple=(0,1,2,3,4,5,6)
result2=my_tuple[:] #起始不写表示从头到尾，步长1可省
print(result2)    结果：(0, 1, 2, 3, 4, 5, 6)

#对str进行切片，从头到尾，步长为2
my_str="1234567"
result3=my_str[::2]
print(result3)    1357

#对str进行切片，从头到尾，步长为-1
my_str="1234567"
result4=my_str[::-1]
print(result4)     7654321等同于将字符串反转


#对list进行切片，3开始，1结束，步长-1
my_list=[0,1,2,3,4,5,6]
result1=my_list[3:1:-1]
print(result1)     [3, 2]


#对元组进行切片，从头到尾，步长-2
my_tuple=(0,1,2,3,4,5,6)
result2=my_tuple[::-2]
print(result2)     (6, 4, 2, 0)
练习：
my_str="万过薪月，员序程马黑来，nohtyp学"
my_str1=my_str[::-1]
print(my_str1)
my_str2=my_str1[9:14]
print(my_str2)
"""


"""
集合
回忆：
列表可修改，支持元素重复且有序
元组、字符串不可修改，支持重复元素且有序
集合定义：
{元素1，2，3，4，5}
定义集合变量
变量名称={元素，元素，元素}
空集合：变量名称=set()

my_set={"xiaoguai","huanglian","age",2,"xiaoguai","huanglian","age",2}
my_set_empty=set()
print(my_set,type(my_set))   结果是： {'huanglian', 'age', 2, 'xiaoguai'} <class 'set'>

集合无序，不支持下标索引
添加新元素：
集合.add(元素) 将指定元素添加到集合内
my_set={"xiaoguai","huanglian","age",2}
my_set.add("python")
print(my_set)   结果 {2, 'age', 'python', 'huanglian', 'xiaoguai'}

移除元素
集合.remove(元素)
my_set={"xiaoguai","huanglian","age",2}
my_set.remove(2)
print(my_set)       结果  {'age', 'xiaoguai', 'huanglian'}

从集合中随机取出元素
集合.pop()从集合中随机取出一个元素
结果：会得到一个元素的结果，同时集合被修改，元素被移除
my_set={"xiaoguai","huanglian","age",2}
element=my_set.pop()
print(element)
print(my_set)  结果  2   {'age', 'huanglian', 'xiaoguai'}

清空集合
集合.clear()

取出两个集合差集
集合1.difference（集合2）  取出集合1和集合2的差集（集合1有而集合2没有的）
得到一个新集合，集合1，2不变
set1={1,2,3}
set2={5,6,3}
set3=set1.difference(set2)
print(set1,set2,set3)   结果 {1, 2, 3} {3, 5, 6} {1, 2}

消除两个集合的差集
集合1.differenc_update(集合2) 在集合1内删除和集合2相同的元素
集合1被修改，集合2不变
set1={1,2,3}
set2={5,6,3}
set1.difference_update(set2)
print(set1,set2)       结果   {1, 2} {3, 5, 6}

两个集合合并
集合1.union(集合2) 将集合1、集合2组成新集合
得到新集合，集合1和集合2不变
set1={1,2,3}
set2={5,6,3}
set3=set1.union(set2)
print(set1,set2,set3)    结果 {1, 2, 3} {3, 5, 6} {1, 2, 3, 5, 6}

统计集合元素数量
len(集合)

只支持for循环
练习：
my_list=["黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","itcast","best"]
my_set=set()
for element in my_list:
    my_set.add(element)
print(my_set)         结果：{'传智播客', 'itheima', 'itcast', '黑马程序员', 'best'}
"""

"""
字典：
存储的键值对
定义字典字面量
{key:value,key:value}
定义字典变量
my_dict={key:value,key:value}
定义空字典
my_dict={}
my_dict=dict()
不可以使用下标索引，通过key值来取得对应的value

my_dict={"lily":99,"cici":88,"zz":89}
score=my_dict["lily"]
print(f"lili的考试分数：{score}")   结果lili的考试分数：99

key和value可以为任意数据类型，除了key不能为字典，字典可以嵌套
stu_score_dict={
    "lily":{
        "chinese":77,
        "math":66,
        "english":72
    },"cici":{
        "chinese": 88,
        "math": 86,
        "english": 76
    },"zz":{
        "chinese": 99,
        "math": 96,
        "english": 82
    }
}
print(stu_score_dict)
grade=stu_score_dict["cici"]["chinese"]
print(grade)
结果：
{'lily': {'chinese': 77, 'math': 66, 'english': 72}, 'cici': {'chinese': 88, 'math': 86, 'english': 76}, 'zz': {'chinese': 99, 'math': 96, 'english': 82}}
88

字典的常用操作

新增元素：
字典[key]=value  字典被修改，新增了元素； 如果key不存在，就是新增元素
my_dict={"lily":99,"cici":88,"zz":89}
my_dict["zwy"]=77
print(my_dict)     结果    {'lily': 99, 'cici': 88, 'zz': 89, 'zwy': 77}

更新元素
字典[key]=value  字典被修改，更新了元素； 如果key存在，就是更新元素（因为字典key不重复）
my_dict={"lily":99,"cici":88,"zz":89}
my_dict["lily"]=77
print(my_dict)      结果  {'lily': 77, 'cici': 88, 'zz': 89}

删除元素
字典.pop(key)     获得指定key的value,同时字典被修改，指定key的数据被删除
my_dict={"lily":99,"cici":88,"zz":89}
grade=my_dict.pop("lily")
print(my_dict)
print(grade)    
结果：
{'cici': 88, 'zz': 89}
99

清空元素
字典.clear()

获取全部的key:
字典.keys()  得到字典中全部的key
my_dict={"lily":99,"cici":88,"zz":89}
name=my_dict.keys()
print(name)     结果： dict_keys(['lily', 'cici', 'zz'])

遍历字典
my_dict={"lily":99,"cici":88,"zz":89}
name=my_dict.keys()
方式1：for key in name:
        print(f"字典的key:{key}")
        print(f"字典的valu：{my_dict[key]}")
方式2：for key in my_dict:
        print(f"字典的key:{key}")
        print(f"字典的valu：{my_dict[key]}")

统计字典的元素数量
len(my_dict)

练习
staff_inf={"王力宏":{"部门":"科技部","工资":3000,"级别":1},
           "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
           "张学友":{"部门":"市场部","工资":7000,"级别":3},
           "林俊杰":{"部门":"科技部","工资":4000,"级别":1},
           "刘德华":{"部门":"市场部","工资":6000,"级别":2},
           }
print(staff_inf)
for name in staff_inf:
    if staff_inf[name]["级别"]==1:
        employee_info_dict=staff_inf[name]
        employee_info_dict["级别"]=2
        employee_info_dict["工资"]+=1000
        staff_inf[name]=employee_info_dict
print(staff_inf)

数据类型通用操作：
最大：max(容器)
最小：min(容器)
类型转换：
容器转列表：list(容器)
容器转字符串：str(容器) 只有字典转字符串的时候value会保留，其他都只保留key
容器转元组：tuple(容器)
容器转集合：set(容器)

容器通用排序功能
sorted（容器，[reverse=True]）
my_list=[3,4,1,5,8]
my_tuple=(4,8,3,5,7)
my_str="dgfsuyfhi"
my_set={7,8,2,3,5}
my_dict={"key6":3,"key2":1,"key7":2,"key9":5,"key1":8}
sorted(my_list,reverse=True)
sorted(my_tuple)
sorted(my_str)
sorted(my_set)
sorted(my_dict)
print(sorted(my_list,reverse=True)) 列表反向排序了
print(sorted(my_tuple))
print(sorted(my_str))
print(sorted(my_set))
print(sorted(my_dict))
结果：
[8, 5, 4, 3, 1]
[3, 4, 5, 7, 8]
['d', 'f', 'f', 'g', 'h', 'i', 's', 'u', 'y']
[2, 3, 5, 7, 8]
['key1', 'key2', 'key6', 'key7', 'key9']

"""

"""
函数的多返回值
def test_return():
    return 1,"hello",True
x,y,z=test_return()
print(x,y,z)   结果:  1 hello True

函数的多种传参方式
函数参数种类：

1.位置参数：调用函数时根据函数定义的参数位置来传递参数
传递的参数和定义的参数的顺序和个数必须一致
def user_info(name,age,gender):
    print(f"名字是{name},年龄是{age},性别是{gender}")
user_info("lili",20,"female")

2.关键字参数
“键=值”形式传递参数
def user_info(name,age,gender):
    print(f"名字是{name},年龄是{age},性别是{gender}")
user_info(name="lili",age=20,gender="female")   关键字传参
user_info(age=20，name="lili",gender="female")   关键字传参，可以调换顺序
user_info("lili",20,gender="female")   关键字传参可以和位置参数混用，但位置参数在前

3.缺省参数
当调用函数时没有传递参数，就会使用默认是缺省参数对应的值，默认的参数写道最后面
def user_info(name,age,gender="男"):
    print(f"名字是{name},年龄是{age},性别是{gender}")
user_info(name="lili",age=20,gender="female")
user_info("Tom",18)     #没有传递gender，所以默认gender为值“男”
结果：
名字是lili,年龄是20,性别是female
名字是Tom,年龄是18,性别是男

4.不定长的参数：也叫可变参数，不确定调用的时候会传递多少个参数（不传参也可以）
不定长参数类型：位置传递，关键字传递

位置传递：
传递的所有参数都会被args变量收集，会根据传进的参数位置合并为一个元组（tuple）
args是元组类型
def user_info(*args):
    print(args)
user_info("Tom")
user_info("Tom",18)
结果：
('Tom',)
('Tom', 18)

关键字传递：
参数是“键=值”形式的情况下，所有的“键=值”都会被kwargs接受，同时根据“键=值”组成字典
def user_info(**kwargs):
    print(kwargs)
user_info(name="tom",age=18,id=110)
结果：
{'name': 'tom', 'age': 18, 'id': 110}

函数作为参数传递：
def test_func(computer):
    result=computer(1,2)
    print(type(computer))
    print(f"计算结果：{result}")
def computer(x,y):
    return x+y
test_func(computer)
结果：
<class 'function'>
计算结果：3

lambda匿名函数：
函数定义中，def关键字可以定义带有名称的函数
lambda关键字可以定义匿名函数（无名称）
有名称的函数可以基于名称重复使用，无名称的匿名函数，只可以临时使用一次
匿名函数用法：
语法：lambda 出入参数：函数体       （只能写一行代码）
lambda是关键字，表示定义匿名函数
传入参数表示匿名函数的形式参数，如：x,y表示接收2哥形式参数
函数体，就是函数的执行逻辑  ps只能写一行，无法写多行代码
def test_func(computer):
    result=computer(1,2)
    print(f"计算结果：{result}")
test_func(lambda x,y:x+y)
"""

"""
文件编码
编码技术：翻译的规则，怎么将内容翻译成二进制，已经如何将二进制翻译回可识别内容

文件的读取操作：
文章、视频、音频、程序代码都可保存为一个文件。
在python中使用open函数可以打卡一个已经存在的文件，或者创建一个新的新文件：
open（name，mode，encoding）
name：要打开的目标文件名的字符串（可包含文件所在的具体路径）
mode：设置文件打开模式：只读r、写入w、追加a等
encoding：编码格式一般是UTF-8
例子：
f=open('python.txt','r',encoding="UTF-8")

read()方法：
文件对象.read（num）
num:表示从文件中读取数据的长度（单位是字节），如果没有传入num,那么表示读取文件中所有的数据

readlines()方法：
按照行的方式把整个文件中的内容进行一次性读取，并且返回是一个列表，每一行内容为一个元素
readline()方法：
一次只读取一行内容

for循环读取文件行
for line in open("文件名","r")

文件.close()关闭文件
time.sleep（505000） 文件暂停执行505000秒

with open用法：
with open("文件名","r") as f:
    f.readlines()
在with open 执行完with open的代码块文件会自动关闭
练习：方法1
f=open("word.txt","r",encoding="UTF-8")
word=f.read()
print(f"文件的内容是：{word}")
count=word.count("itheima")
print(f"itheima出现的次数{count}")
f.close()

f=open("word.txt","r",encoding="UTF-8")
count=0
for line in f:
    line=line.strip() #去掉开头结尾的空格和换行符/n
    words=line.split(" ")
    for word in words:
        if word=="itheima":
            count+=1
print(f"itheima出现的次数{count}")
f.close()

文件的写入操作：
文件写入：f.write("hello world")
内容刷新
f.flush()

直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
当调用flush的时候，内容会真正写入文件
这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写磁盘）

打开一个不存在的文件
f=open("t.txt","w",encoding="UTF-8")
f.write("hello world")
f.flush() #将内存积攒中的内容，写入硬盘的文件中
f.close()   #close方法，内置了flush功能

打开一个存在的文件，会清空原有内容
f=open("t.txt","w")
f.write("黑马程序员")
f.flush() 

文件的追加,不会清空原有文件
f=open("t.txt","a")
f.write("itheima")
f.flush()
追加写入方法和w方法一样
"""

"""
异常的捕获：异常处理
作用：提前假设某处会出现异常，做好提前啊准备，出现异常的时候有新的处理方法
语法：
try:
    可能发生的错误代码
except:
    如果出现异常执行的代码
   
捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了变量名称未定义的异常")

捕获多个异常
try:
    1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量名称未定义的异常 或者除以0异常")

捕获所有异常
try:
    print(name)
except Exception as e:
    print("出现了异常")

异常else：
表示如果没有异常需要执行的代码
try:
    print("hello")
except Exception as e:
    print("出现了异常")
else:
    print("没有异常")
    
finally表示无论是否异常都要执行的代码，比如关闭文件：
try:
    f=open("123.txt","r")
except Exception as e:
    print("出现了异常")
    f=open("123.txt","w")
else:
    print("没有异常")
finally:
    f.close()
 
异常的传递性
def func1():
    print("func1开始执行")
    num=1/0
    print("func1结束执行")
#定义一个不会出现异常的方法，调用上面的方法
def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")
#定义一个方法，调用上面的方法
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常的信息是{e}")
main()
"""

"""
模块：可以当作一个工具包，模块就是一个python文件，里面有类、函数、变量等
模块的导入方式：
[from 模块名] import [模块/类/变量/函数/*] [as 别名]  []中可以不写
语法：
import 模块名
import 模块名1，模块名2
模块名.功能名（）
方式一：
# import time
# print("开始")
# time.sleep(5)
# print("结束")

方式二：
from time import sleep      使用from导入time的sleep功能
print("开始")
sleep(5)
print("结束")

方式三：
from time import *     *表示全部功能
print("开始")
sleep(5)
print("结束")

方式四：
import 模块名 as 别名                   模块定义别名
from 模块名 import 功能名 as 别名        功能定义别名
import time as t
print("开始")
t.sleep(2) 
print("结束")

from time import sleep as sl
print("开始")
sl(2) 
print("结束")
"""

"""
自定义模块：模块名称就是文件名称
两种方式
import my_module1
my_module1.test(1,2)

from my_module1 import test
test(1,2)

注意:导入不同模块的同名功能，后导入的功能会把前面的覆盖，会运行后面的导入功能

__main__变量：
内部可以测试函数，外部不运行

__all__变量：
如果一个模块文件中有__all__变量，当使用"from xxx import *"导入时，只能导入这个列表中的元素
from my_module1 import *
test_a(1,2)
# test_b(2,1)
"""

"""
python包就是一个文件夹
语法方式一：
import 包名.模块名
包名.模块名.目标
import my_package.my_mudole1
import my_package.my_module2
my_package.my_mudole1.info_print1()
my_package.my_module2.info_print2()

from my_package import my_mudole1
from my_package import my_module2
my_mudole1.info_print1()
my_module2.info_print2()

from my_package.my_mudole1 import info_print1
from my_package.my_module2 import info_print2
info_print1()
info_print2()

方式二：
在包里面__init__.py文件夹中添加__all__=[]控制允许导入的模块列表
__all__=["my_module1"]

from my_package import *
my_module1.info_print1()

"""

"""
第三方包
import my_utils.str_util
from my_utils import file_util
print(my_utils.str_util.str_reverse("黑马程序员"))
file_util.print_file_info("D:/test_append.txt")
"""
"""
理解使用对象完成数据组织的思路
使用对象组织数据
1.在程序中设计表格，我们称之为：设计类
class Student:
    name=None
2.在程序中打印生产表格，我们称之为：创建对象
#基于类创建对象
stu_1=Student()
stu_2=Student()
3.在程序中填写表格，我们称之为：对象属性赋值
stu_1.name="周杰伦"     #为学生1对象赋予名称属性值
stu_2.name="林林"       #为学生2对象赋予名称属性值
class Student:
    name=None
    gender=None
    nationality=None
    native_place=None
    age=None
    
stu_1=Student()

stu_1.name="linlin"
stu_1.gender="male"
stu_1.nationality="china"
stu_1.native_place="cq"
stu_1.age=19

print(stu_1.age)
print(stu_1.native_place)
print(stu_1.gender)
print(stu_1.name)
print(stu_1.nationality)


类的定义和使用：
可以使用类去封装属性，并基于类创建出一个个的对象来使用
具体语法:
class 类名称:      class是关键字，表示要定义类
    类的属性       定义在类中的变量（成员变量）
    类的行为       定义在类中的函数（成员方法）    类里面的函数
创建类对象的语法：
对象=类名称()
成员方法的定义语法

def 方法名(self,形参1,形参2,···形参n):
    方法体
self关键字：
用来表示类对象自身的意思
当我们使用类对象调用方法的时候，self会自动被python传入
在方法的内部，想要访问类的成员变量，必须使用self
在传入参数的时候self是透明的
class Student:
    name=None
    def say_hi(self):
        print(f"大家好，我是{self.name},欢迎大家多多关照")
    def say_hi2(self,msg):
        print(f"大家好，我是：{self.name},{msg}")
stu=Student()
stu.name="lily"
stu.say_hi2("哎哟不错哟")

stu2=Student()
stu2.name="cici"
stu2.say_hi2("看好你")

类和对象
设计类，基于类创建对象，由对象做具体的工作。
#设计一个闹钟类
class Clock:
    id=None
    price=None

    def ring(self):
        import  winsound
        winsound.Beep(2000,3000)

#创建对象，让他干活
clock1=Clock()
clock1.id="003023"
clock1.price=12.3
print(f"闹钟id：{clock1.id},价格：{clock1.price}")   闹钟id：003023,价格：12.3

构造方法
用__init__方法
在创建类对象（构造类）的时候，会自动执行
在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
    name=None
    age=None
    tel=None

    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print("Student类创建了一个类对象")

stu1=Student("zz",5,1239375)
print(stu1.name,stu1.tel,stu1.age)        Student类创建了一个类对象     zz 1239375 5

class Student:

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(f"学生{i}信息录入完成，信息为 学生姓名{name},年龄{age},地址{address}")
for i in range(1,11):
    print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
    name=input("请输入学生姓名： ")
    age=int(input("请输入学生年龄： "))
    address=input("请输入学生地址： ")
    stu=Student(name,age,address)
print(f"学生{i}信息录入完成,信息为: 学生姓名：{stu.name},年龄：{stu.age},地址：{stu.address}】")

魔术方法
类似__init__这样的类方法，各自有各自特殊的功能，这些内置方法我们称之为魔术方法
1.__str__字符串方法
当类对象需要被转换成字符串时，会输出内存地址，这个时候通过__str__方法控制类转换成字符串的行为（就是我们想要的信息）
2.__eq__比较运算符方法
传入参数other，另一个对象
返回值True 或者False
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Student类对象，name:{self.name}, age:{self.age}"

    def __eq__(self, other):
        return self.age==other.age

stu1=Student("lily",6)
stu2=Student("cici",6)
print(stu1==stu2)

封装
将现实世界的属性和行为，封装到类中，描述为成员变量和成员方法。其实在程序中的成员变量和成员方法就是封装，就完成了程序对现实世界事物的描述。
私有成员：
现实世界有不公开的属性和行为，程序中也有就要做私有成员
类中提供了私有成员的形式支持
私有成员变量和私有成员方法。
私有成员变量：变量名以__开头
私有成员方法：方法名以__开头
class Phone:
    __current_voltage=None
    def __keep_single_core(self):
        print("让cpu以单核运行")
phone=Phone()
phone.__keep_single_core()
print(phone.__current_voltage)   会报错
类对象无法访问私有成员，但是其他公开的成员方法是可以使用这些私有成员方法的
class Phone:
    __current_voltage=2

    def __keep_single_core(self):
        print("让cpu以单核运行")

    def call_by_5G(self):
        if self.__current_voltage>=1:
            print("5g通话已经开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法用5G通话，设置为单核运行省电")

phone=Phone()
phone.call_by_5G()

class Phone:
    __is_5g_enable=None

    def __check_5g(self):
        if self.__is_5g_enable==True:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone=Phone()
phone.call_by_5g()

继承
继承表示：将从父类那里继承（复制）成员变量和方法不含私有成员
继承分为单继承和多继承，下面为单继承
class 类名(父类名):
    类内容体
    
class Phone:
    IMEI=None
    producer="heima"

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id="1002"

    def call_by_5g(self):
        print("2022新功能：5g通话")

phone=Phone2022()
print(phone.producer)
phone.call_by_5g()
phone.call_by_4g()        heima   2022新功能：5g通话    4g通话
    
    
多继承就是一个子类继承多个父类
class 类名（父类1，父类2.···，父类n）：
    类内容体
class Phone:
    IMEI=None
    producer="heima"

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id="1002"

    def call_by_5g(self):
        print("2022新功能：5g通话")

phone=Phone2022()
print(phone.producer)
phone.call_by_5g()
phone.call_by_4g()

class NFCReader:
    nfc_type="第五代"
    producer="HM"

    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type="hwyk"

    def control(self):
        print("红外遥控开启")

class Myphone(Phone,NFCReader,RemoteControl):
    pass  #补全语法，不想写新功能了

phone=Myphone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()
print(phone.producer)

heima
2022新功能：5g通话
4g通话
4g通话
NFC读卡
NFC写卡
红外遥控开启
heima

多继承中，对于同名的成员，谁先继承谁的优先级更高，从左到右优先级

复写：
子类继承父类的成员属性和成员方法后，如果对其不满意，可以进行复写
在子类中重新定义同名的属性或者方法即可
class Phone:
    IMEI=None
    producer="ITCAST"
    def call_by_5g(self):
        print("使用5g网络通话")
class Myphone(Phone):
    producer = "itheima"
    def call_by_5g(self):
        print("开启CPU单核模式")
        print("使用5G通话")
        print("关闭CPU单核模式省电")
phone=Myphone()
phone.call_by_5g()
print(phone.producer)
开启CPU单核模式
使用5G通话
关闭CPU单核模式省电
itheima

调用父类的同名成员
一旦复写父类成员，那么类对象调用成员的时候，会调用复写后的新成员
如果要调用父类原始成员需要特殊调用方法
方法1：
使用成员变量： 父类名.成员变量
使用成员方法： 父类名.成员方法(self)
方法2：
使用super()调用父类成员
使用成员变量： super().成员变量
使用成员方法： super().成员方法()
class Phone:
    IMEI=None
    producer="ITCAST"
    def call_by_5g(self):
        print("使用5g网络通话")
class Myphone(Phone):
    producer = "itheima"
    def call_by_5g(self):
        print("开启CPU单核模式")
        print(f"父类的厂商是：{Phone.producer}")
        super().call_by_5g()
        print("关闭CPU单核模式省电")
phone=Myphone()
phone.call_by_5g()
print(phone.producer)
开启CPU单核模式
父类的厂商是：ITCAST
使用5g网络通话
关闭CPU单核模式省电
itheima

为变量设置类型注解
变量: 类型

函数和方法的形参类型注解
def 函数方法名（形参名：类型，形参名：类型）：
    pass
def add(x:int,y:int):
    return x+y
add()
对函数（方法）返回值进行注解
def 函数方法名（形参名：类型，形参名：类型）->返回值类型：
def fun(data:list)-> list:
    return data

Union联合注解
导入包 ： from typing import Union
使用：    Union[类型，类型]

多态：
使用同样的行为（函数），传入不同的对象，会得到不同的状态
堕胎常作用在继承关系上
比如：
函数（方法）形式参数声明接收父类对象
实际传入父类的字类对象继续工作。
用父类做定义声明，子类做实际工作
用以获得同一行为的不同状态
抽象类
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

list1 = append_to_list(1)
list2 = append_to_list(2)
print(list1)  # 输出？
print(list2)  # 输出？


def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []  # 每次调用都创建一个新的列表
    my_list.append(value)
    return my_list

list1 = append_to_list(1)  # 返回一个新的列表 [1]
list2 = append_to_list(2)  # 返回另一个新的列表 [2]

print(list1)  # 输出：[1]
print(list2)  # 输出：[2]
"""

import tkinter
tkinter._test()