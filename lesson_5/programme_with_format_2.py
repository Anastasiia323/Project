word_1 = input('Введите первое слово: ')
word_2 = input('Введите второе слово: ')

final_phrase = '{} {}'.format(word_1, word_2)
final_phrase_1 = '!{} ! {}!'.format(word_2, word_1)
final_phrase_2 = '{0} {1}'.format(word_1, word_2)
final_phrase_3 = '!{1} ! {0}!'.format(word_1, word_2)

print(final_phrase)
print(final_phrase_1)
print(final_phrase_2)
print(final_phrase_3)
