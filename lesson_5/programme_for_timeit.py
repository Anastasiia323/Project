import timeit
import time

start = time.time()

def write_the_number():
    a = int(input("Введите число: "))
    summa = 0
    for i in range(0, a+1):
        summa = summa + i
        print(summa)

write_the_number()

end = time.time()

print(end)

# практика модуля timeit

print(timeit.timeit('x = sum([1, 2, 3, 4, 5])'))











