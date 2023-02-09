first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}
third_dict = {}

for k, v in first_dict.items():
    third_dict[k] = [v, second_dict.get(k)]

for k, v in second_dict.items():
    third_dict[k] = [first_dict.get(k), v]

print(third_dict)
