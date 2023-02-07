import json

"""Согласно заданию, создала словарь, где шестзначному id присвоила 
им знаечения в виде кортежа, состоящего из имени и возраста"""

name1, name2, name3, name4, name5 = ('Anstasiia', 'Sergei', 'Mariia', 'Ann', 'Joe')
age1, age2, age3, age4, age5 = (32, 33, 17, 45, 30)


new_dict = {
    100001: (name1, age1),
    100002: (name2, age2),
    100003: (name3, age3),
    100004: (name4, age4),
    100005: (name5, age4)
}

with open('new_dict_file.json', 'wt') as write_file:
    json.dump(new_dict, write_file, indent=2)

write_file.close()




