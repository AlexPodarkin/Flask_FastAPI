import time
import random


# def count_down(n):
#     for i in range(n, 0, -1):
#         print(i)
#         time.sleep(1)
#
#
# count_down(5)


# def slow_function():
#     print('Начало функций')
#     time.sleep(5)
#     print('Конец функции')
#
#
# print('Начало программы')
# slow_function()
# print('Конец функции')


def long_running():
    for i in range(5):
        print(f'Выполнение задачи {i}')
        time.sleep(random.randint(1, 3))


def main():
    print('Начало работы')
    long_running()
    print('Конец программы')


main()
