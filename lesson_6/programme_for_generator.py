import datetime
import time

def some_func():
    def print_date(count: int) -> list:
        a = datetime.datetime.now()
        b = datetime.timedelta(seconds=1)   # использовала данный модуль, так как он не задерживает программу, но при этом прибавляет секунды
        my_list = [str(a + i * b) for i in range(count)]     # прибавила, используя формулу арифметической прогрессии
        return my_list

    print(print_date(2))
some_func()








