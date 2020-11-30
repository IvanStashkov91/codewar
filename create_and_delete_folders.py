'''
1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
'''
import os

def create_dir():
    for i in range(1, 10):
        dir_name = f'dir_{i}'
        os.mkdir(dir_name)

def delete_dir():
    for i in range(1, 10):
        dir_name = f'dir_{i}'
        os.rmdir(dir_name)

create_dir()
delete_dir()
