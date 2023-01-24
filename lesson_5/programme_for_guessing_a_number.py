import random
number_to_guess = random.randint(1, 100)
our_number = 0

while our_number != number_to_guess:
    our_number = int(input('Введите число: '))

    if our_number > number_to_guess:
        print('Не угадали, нужно меньше')

    elif our_number < number_to_guess:
        print('Не угадали, нужно больше')

    else:
        our_number = number_to_guess
        print('Вы угадали')















