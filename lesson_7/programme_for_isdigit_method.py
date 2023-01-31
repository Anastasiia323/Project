from beartype import beartype

@beartype
def analyze_the_string(my_number: str) -> str:
    """Определяю, содержатся ли во входящей строке цифры
    и, в зависимости от результата, привожу к float"""
    my_number_check = my_number.isdigit()
    my_number_sym_replace = my_number.replace(',', '.')
    if '.' in my_number:
        if my_number[0] != '-':
            return f'Вы ввели положительное дробное число {float(my_number)}'
        else:
            return f'Вы ввели отрицательное дробное число {float(my_number)}'

    if ',' in my_number:
        my_number_sym_replace = my_number.replace(',', '.')
        if my_number[0] != '-':
            return f'Вы вввели положительное дробное число {float(my_number_sym_replace)}'
        else:
            return f'Вы ввели отрицательное дробное число {float(my_number_sym_replace)}'

    if my_number_check:
        return f'Вы ввели положительное целое число {int(my_number)}'
    else:
        if my_number[0] == '-':
            return f'Вы ввели отрицательное целое число {round(float(my_number))}'
        else:
            return 'Вы ввели некорректное число'


string_to_exam = '-9.2'

print(analyze_the_string(string_to_exam))