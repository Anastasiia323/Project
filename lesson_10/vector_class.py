class Vector:
    def __init__(self, a, b):
        self.a = a   # arguments of object
        self.b = b

    def length(self):
        distance = (((self.b[0] - self.a[0]) ** 2)
                    + ((self.b[1] - self.a[1]) ** 2)) * 0.5
        return distance

    def __eq__(self, other):
        print(self)
        print(other)
        return self.length() == other.length()

    def __gt__(self, other):
        print(self)
        print(other)
        return self.length() > other.length()

    def __ge__(self, other):
        print(self)
        print(other)
        return self.length() >= other.length()


v1 = Vector((1, 3), (2, 4))
v2 = Vector((5, 7), (6, 1))

print(v1.length())
print(v2.length())
print(v1 <= v2)
