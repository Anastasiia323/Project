# string and bool methods test
# str.capitalize()

word1 = 'Hello, Everybody'
word2 = word1.capitalize()

print(word2)

# str.upper()

phrase_1 = "We study python"
phrase_1_upper = phrase_1.upper()

print(phrase_1_upper)

phrase_2 = "Who study python?"
phrase_3 = phrase_2.replace('python', 'English')
phrase_4 = phrase_2.replace('thon', '****')

print(phrase_3)
print(phrase_4)

# str.count()

string = 'У Лукоморья дуб срубили'
final_string = string.count('дуб', 0, -1)
print(final_string)

# str.find()

string1 = 'Hello, World'
symbol = string1.find('d', 1, 5)

print(symbol)

# str.isalpha()

string2 = string1.isalpha()

print(string2)

# str.isdigit()

card_number = '12345678.'
is_card_number_digit = card_number.isdigit()

print(is_card_number_digit)

# str.rjust()

phrase_5 = "Hello"
phrase_6 = phrase_5.rjust(6, '-')

print(phrase_6)

# str.split()

phrase_7 = '1, 2,3,4, 5,6'
phrase_8 = phrase_7.replace(' ', '').split(",")

print(phrase_8)

# str.join()

letters = 'ABCDEFG'
new_letters = ','.join(letters)

print('Вот такие буквы:', new_letters)

# float methods test
# float.is_integer()
# float.hex()
# int(float)
# round(float)
# random

number1 = 4.9
number2 = number1.is_integer()
number2_1 = number1.hex()
number2_2 = int(number1)
number2_3 = round(number1)

print(number2)
print(number2_1)
print(number2_2)
print(number2_3)

# random

import random
random.random()

print(random.random())

# int methods test
# float(int)
# abs(int)
# pow()

number3 = 5
number3_1 = float(number3)
number_4 = -8
nuber_5 = abs(number_4)
number_6 = pow(number3, 4)

print(number3_1)
print(nuber_5)
print(number_6)














