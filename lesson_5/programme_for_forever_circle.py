a = input('Введите ваше имя: ')
b = int(input('Введите ваш возраст: '))

while b >= 0:
    if b == 0 or b is str:
        print('Ошибка, повторите ввод.')

    elif b < 0:
        print('Ошибка, повторите ввод.')

    elif b in range(9):
        print(f'Привет, шкет {a}!')

    elif b in range(10, 19):
        print(f'Привет, как жизнь, {a}?')

    elif b > 10 and b < 100:
        print(f'Что желаете, {a}?')

    else:
        print(f'{a}, вы лжёте, в наше время столько не живут!')