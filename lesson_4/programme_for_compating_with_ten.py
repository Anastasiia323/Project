a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a > 10 and b > 10:   # a or b > 10 это неправильно, нужно каждой переменной давать условие
    print(f'Вы ввели: {a} и {b}, оба числа больше 10')

elif a > 10 or b > 10:
    print(f'Вы ввели: {a} и {b}, одно из чисел больше 10')

else:
    if not bool(a):
        print('Условие с помощью преобразования типов')  # TODO изучить основы булевой алгебры





