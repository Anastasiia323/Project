"""Записываю значение переменной в текстовый файл"""

file_to_func = open('new_txt_file', 'r')
# Открываю на чтение, чтобы использовать в функции

"""Создаю функцию для обхода файла"""


def what_count():
    lines = file_to_func.readline()
    summa = 0
    for i in lines:
        if i.lower() == letter.lower():
            summa = summa + 1
    return f'Буква встречается в тексте {summa} раз/раза'


letter = input('Write the letter: ')

print(what_count())

file_to_func.close()
