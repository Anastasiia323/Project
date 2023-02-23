"""Записываю значение переменной в текстовый файл"""


def what_count():
    with open('new_txt_file', 'r') as file_to_func:
        reader = file_to_func.readline()
    summa = 0
    for line in reader:
        if letter.lower() in line:
            summa += 1
    return f'Буква встречается в тексте {summa} раз/раза'


letter = input('Write the letter: ')

print(what_count())
