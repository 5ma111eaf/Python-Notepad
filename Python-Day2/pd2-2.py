import math

# 于大部分都是string类型所以我取部分来检测它们的数据类型

city = 'chine'
age = 20
is_married = False
is_true = 'yes'

print(type(city), type(age), type(is_married), type(is_true))

firstname = len('5ma11')
lastname = len('1eaf')
if firstname == lastname:
    print("长度相同")
elif firstname > lastname:
    print("firstname > lastname")
else:
    print("firstname < lastname")


num_one = 5
num_two = 6

total = num_one + num_two

diff = num_one - num_two

product = num_one * num_two

divisor = num_one / num_two

remainder = num_one % num_two

exp = num_one ** num_two

floor_division = num_one // num_two

r = 30
area_of_circle = math.pi * r ** 2
circum_of_circle = 2 * math.pi * r

print(area_of_circle, circum_of_circle)

r = int(input("请输入半径数值:"))
area_of_circle = math.pi * r ** 2
print(area_of_circle)


firsname = input("请输入你的名")
lastname = input("请输入你的姓")
city = input("请输入你的国家")
age = int(input("请输入你的年龄"))


help('keywords')