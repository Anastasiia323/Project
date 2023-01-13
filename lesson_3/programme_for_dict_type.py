new_dict = {'number1': 1, 'number2': 2} # типы создания словарей
dict_2 = dict(number3='3', number4='4') # типы создания словарей
dict_3 = dict.fromkeys(['phrase1', 'phrase2'], 'Hello, World!') #типы создания словарей
dict_4 = {a: a ** 2 for a in range(7)} # возвела каждое значение во вторую степень в отрезке от 0 до 7
dict_5 = {1: 'Hi', 2: 'Bye', 3: "I don't know"}
dict_5[4] = 'Go away' # добавила ещё один ключ и его значение в предыдущий словарь


print(new_dict)
print(dict_2)
print(dict_3)
print(dict_4)
print(dict_5)
print(dict_5[1])
print(dict_5[3])
print(dict_5)

dict_to_test = {1: 'Ivanov', 2: 'Ivan', 3: 'Ivanovich'}
dict_to_test_1 = dict_to_test.copy()   # скопировала существующий словарь в новый словарь
dict_to_test.update({4: 'Hi'}) # добавила дополнительный ключ и значение в первоначальный словарь


print(dict_to_test.get(1)) # вывела на экран значение первого ключа
print(dict_to_test.keys()) # вывела на экран все ключи
print(dict_to_test.pop(4)) # вывела значение ключа 4

