import json
import csv


new_file = open('new_dict_file.json')  # открываю json документ как объект python
my_dict = json.load(new_file)


a = {}  # создаю пустой словарь, в который запишу новые ключи и значения

csv_file = open('new_csv_file.csv', 'w', newline='\n')       # открываю на запись документ csv, задаю значения заголовкам
fields = ['id', 'name', 'age', 'number']
writer = csv.DictWriter(csv_file, fields)
writer.writeheader()

for k, v in my_dict.items():   # обхожу словарь
    name = v[0]
    age = v[1]
    id = k
    number = 88005553535      # добавляю дополнительную колонку с номером телефона
    # создаю строчку записи в csv
    a = {'id': id, 'name': name, 'age': age, 'number': number}
    writer.writerow(a)

csv_file.close()