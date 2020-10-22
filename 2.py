# DZ-1

# list = [1, -8, 'One', 4.3]
#
# def my_type(el):
#     for el in range(len(list)):
#         print(type(list[el]))
#     return
#
# my_type(list)




#DZ-2

# count = int(input("Введите количество элементов: "))
# my_list = []
# i = 0
# el = 0
# while i < count:
#     my_list.append(input("Введите следующее значение: "))
#     i += 1
#
# for elem in range(int(len(my_list)/2)):
#         my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
#         el += 2
# print(my_list)




#DZ-3

# season_list = ['Зима', 'Весна', 'Лето', 'Осень']
# season_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
# month = int(input("Введите номер месяца: "))
#
# if month ==1 or month == 12 or month == 2:
#         print(season_dict.get(1))
#         print(season_list[0])
#
# elif month == 3 or month == 4 or month ==5:
#     print(season_dict.get(2))
#     print(season_list[1])
#
# elif month == 6 or month == 7 or month == 8:
#     print(season_dict.get(3))
#     print(season_list[2])
#
# elif month == 9 or month == 10 or month == 11:
#     print(season_dict.get(4))
#     print(season_list[3])
#
# else:
#     print("Месяца с таким номером не существует")




# DZ-4

# my_str = input("введите несколько слов через пробел: ")
# word = []
# num = 1
#
# for el in range(my_str.count(' ') + 1):
#     word = my_str.split()
#     if len(str(word)) <= 10:
#         print(f" {num} {word [el]}")
#         num += 1
#     else:
#         print(f" {num} {word [el] [0:10]}")
#         num += 1




# DZ-5

# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг - {my_list}")
# digit = int(input("Введите число (Для выхода введите 0): "))
#
# while digit != 0:
#     for el in range(len(my_list)):
#         if my_list[el] == digit:
#             my_list.insert(el + 1, digit)
#             break
#         elif my_list[0] < digit:
#             my_list.insert(0, digit)
#         elif my_list[-1] > digit:
#             my_list.append(digit)
#         elif my_list[el] > digit and my_list[el + 1] < digit:
#             my_list.insert(el + 1, digit)
#     print(f"Список - {my_list}")
#     digit = int(input("Введите новое число: "))




#DZ-6
#К сожалению не понял как сделать 6е задание. Если не сложно распишите пожалуйта.