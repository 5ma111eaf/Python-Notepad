import math


int_number = 10 #整数
float_number = 3.14 #浮点数
complex_number = 2 + 4j #复数
str_date = '5ma111eaf' #字符串
list_date = [1, 2, 3] #列表
dictionary_date = {'a': 1, 'b': 2, 'c': 3} #字典
set_date = {1, 2, 3} #集合
tuple_date = (1, 2, 3) #元组

print(type(int_number))
print(type(float_number))
print(type(complex_number))
print(type(str_date))
print(type(list_date))
print(type(dictionary_date))
print(type(set_date))
print(type(tuple_date))


#求(2,3)和(10,8)之间的欧几里得距离
a = 2
b = 3
c = 10
d = 8

aa = (c - a) ** 2 + (d - b) ** 2
print("欧几里得距离为:", math.sqrt(aa))

#欧几里得距离公式是，xy之间差的平方相加，求出的根号值就是欧几里得的距离了。