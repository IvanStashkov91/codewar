#1: Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list1 = ['apple', 'pear', 'orange', 'pineapple']
list2 = ['orange', 'banana', 'apple', 'pear']

result = [fruit for fruit in list1 if fruit in list2]
print(result)

#2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
#Элемент кратен 3,
#Элемент положительный,
#Элемент не кратен 4.

numbers = [5, 6, -9, 6, 4, 5, 1, 20, 21, 18, -15, 4, -98, 4, 8, 0]

result = [number for number in numbers if number > 0 and number % 3 == 0 and number % 4 != 0 ]
print(result)

#3. Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список
# из квадратных корней чисел (если число положительное) и
# самих чисел (если число отрицательное) и
# возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный спи сок не должен измениться.
import math

def function(list):
    result = [math.sqrt(number) if number > 0 else number for number in list]
    return result

list = [1, -3, 4, 5, 9, 0, -8, -16, 8, 1, 1, 1, 5.5]

print(function(list))
print(list)

# 4. Написать функцию которая принимает на вход число от 1 до 100.
# Если число равно 13, функция поднимает исключительную ситуации ValueError
# иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат,
# который вернула функция. Обработать возможность возникновения исключительной ситуации,
# которая поднимается внутри функции.

def square_number(number):
    if number == 13:
        raise ValueError('Not lucky number')
    elif number < 0 or number > 100:
        raise Exception('From 0 to 100')
    else:
        return pow(2, number)


one_number = int(input('Enter the number\n>>>'))

try:
    print(square_number(one_number))
except ValueError:
    print('Not 13')
except Exception:
    print('from 0 to 100')








