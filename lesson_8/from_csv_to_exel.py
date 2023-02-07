import csv
import openpyxl as openpyxl
from openpyxl import workbook, Workbook

def transpose(mat):    # создаю функцию для транспонирования исходной таблицы
    matrix = []
    for i in range(len(mat[0])):
        matrix.append(list())
        for j in range(len(mat)):
            matrix[i].append(mat[j][i])
    return matrix

new_file = open('new_csv_file.csv')     # открываю файл csv на чтение
my_file_to_work = csv.reader(new_file)

book = openpyxl.Workbook()    # создаю новый лист и активирую его
sheet = book.active

for row in my_file_to_work:     # заполняю лист данными из csv файла
    sheet.append(row)

sheet.delete_cols(3, 1)    # удаляю колонку с возрастом

a = list(sheet.values)    # меняю тип данных у таблицы для дальнейшего транспонирования

t = transpose(a)      # вызываю функцию


for row in t:           # добавляю в таблицу новый данные
    sheet.append(row)

sheet.delete_rows(1, 6)          # и удаляю старые
sheet.move_range('A1:F3', rows=1)     # смешаю вниз на одну строку, чтобы добавить в освободившуюся строк 'person'
sheet['B1'].value = 'person1'
sheet['C1'].value = 'person2'
sheet['D1'].value = 'person3'
sheet['E1'].value = 'person4'
sheet['F1'].value = 'person5'

book.save('my_file.xlsx')
book.close()
