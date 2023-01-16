import sys

a = 'Hello, World!'
b = 'Hello, World!'
c = 'Hello, World!'
d = list('12345')
e = tuple('12345')


a1 = list('Hello, World!')
b1 = a1.copy()
c1 = set('Hello, World!')
d1 = sys.intern(str(list('12345'))[1:-1])
e1 = sys.intern(str(tuple('12345'))[1:-1])

print(id(a1), id(b1))
print(id(c1))
print(id(d1), id(e1))






