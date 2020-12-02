'''
2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
'''
import random

def random_item_list(input_list):
    if input_list:
        return random.choice(input_list)

if __name__ == '__main__':
    print(random_item_list([1, 2, 3, 4, 5]))