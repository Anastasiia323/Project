import time
from datetime import datetime

def dec_func(what_number):
    """Cоздаю декоратор для функции"""
    def wrapper():
        """Создаю обёртку"""
        start = time.time()
        what_number()
        end = end = time.time() - start
        print(f'Время выполнения программы {end}')
    return wrapper()

"""Определяю декорируемую функцию"""
@dec_func
def what_number() -> str:
    """Определяю, чётное число или нет с помощью lambda-функции"""
    number_2 = int(input('Введите число: '))
    result_2 = lambda number_2 : f'Число чётное' if number_2 % 2 == 0 else f'Число нечётное'
    return result_2(number_2)