class Alphabet:

    def __init__(self, end, lower):
        self.end = end
        self.lower = lower

    def __iter__(self):
        self.start_1 = ord('a')
        self.start_2 = ord('A')

        return self

    def __next__(self):
        if self.lower:
            if self.start_1 == ord(self.end) + 1:
                raise StopIteration
            else:
                result = self.start_1
                self.start_1 += 1
            return chr(result)
        else:
            if self.start_2 == ord(self.end) + 1:
                raise StopIteration
            else:
                result = self.start_2
                self.start_2 += 1
            return chr(result)


a = Alphabet('m', True)

for letter in a:
    print(letter)
