import timeit

def write_the_number():
    a = range(2, 10)
    for i in a:
        print(i)

write_the_number()

print('Время работы функции:', timeit.timeit(stmt='write_the_number()', number=1000, globals=globals()))
















