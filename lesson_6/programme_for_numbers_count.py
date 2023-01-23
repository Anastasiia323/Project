def find_number(numbers_list, number):
    summa = 0
    for k, v in numbers_list.items():
        if v == number:
            summa = summa + 1
    return summa


number_list = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 8, 8: 6, 9: 9, 10: 11, 11: 6, 12: 6}


print(find_number(number_list, 6))




