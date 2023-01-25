# from beartype import beartype

def what_number() -> str:
    """Определяю, чётное число или нет с помощью lambda-функции"""
    number_2 = int(input('Введите число: '))
    result_2 = lambda number_2 : f'Число чётное' if number_2 % 2 == 0 else f'Число нечётное'
    return result_2(number_2)

print(what_number())

#
# beartype
#
# @beartype
# def what_number() -> None:
#     """Создание lambda-функции, которая определяет, чётное число или нет"""
#     number = int(input('Введите число: '))
#     result = lambda number: number % 2
#
#     while result(number) == 1:
#         print('Число нечётное')
#         number = int(input('Введите число: '))
#     else:
#         print('Число чётное')
#
#     result(number)
#
# what_number()
