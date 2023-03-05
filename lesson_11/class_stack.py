from collections import deque


class Stack:
    def __init__(self):
        self.collection = deque()

    def push(self, element):
        self.collection.append(element)
        return self.collection

    def pop(self):
        last_element = self.collection[-1]
        if len(self.collection) == 0:
            return None
        else:
            self.collection.remove(last_element)
            return self.collection

    def is_empty(self):
        if len(self.collection) == 0:
            return True
        else:
            return False

    def peek(self):
        last_element = self.collection[-1]
        if len(self.collection) == 0:
            return None
        else:
            return last_element


my_stack = Stack()

print(my_stack.push('n'))
print(my_stack.push('m'))
print(my_stack.pop())
print(my_stack.is_empty())


def is_closed():
    my_stack.push(a)
    if '()' and '[]' and '{}' in a:
        return True
    elif '(' or '[' or '{' in a:
        return False
    elif ')' or ']' or '}' in a:
        return False


a = input('Write the string: ')

print(is_closed())
