# easy_1
# name = input('Введите имя: ')
# age = int(input('Введите возраст: '))
# city = input('Введите город, в котором проживаете: ')
#
# def func(name, age, city):
#     print(name, age,'год(а), проживает в городе', city)
#
# func(name, age, city)

# easy_2
# num_1 = input('Введите первое число: ')
# num_2 = input('Введите второе число: ')
# num_3 = input('Введите третье число: ')
#
# def my_max(a,b,c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)
#
# my_max(num_1, num_2,num_3)

# easy_3

# list_1 = []
#
# def my_args(*args):
#     for x in args:
#         list_1.append(x)
#         list_1.sort(key=len)
#     return list_1[-1]
#
# fun = my_args('423', 'abc234', 'a', 'abcdefghklmno', '22', '123456789123')
# print(fun)