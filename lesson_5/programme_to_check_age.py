a = input('Введите ваше имя: ')
b = input('Введите ваш возраст: ')

if b == 0 or b is not int:
    print('Ошибка, повторите ввод.')

elif b < 0:
    print('Ошибка, повторите ввод.')  # TODO узнать, как сократить код с большим количеством elif

elif b in range(9):
    print(f'Привет, шкет {a}!')

elif b in range(10, 19):
    print(f'Привет, как жизнь, {a}?')

elif b > 10 and b < 100:
    print(f'Что желаете, {a}?')

else:
    print(f'{a}, вы лжёте, в наше время столько не живут!')

