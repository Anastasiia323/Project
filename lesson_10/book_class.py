class Book:
    def __init__(self, name, description, pages, author, price):
        self.name = name
        self.description = description
        self.pages = pages
        self.author = author
        self.price = price

    def __gt__(self, other):
        return self.pages > other.pages

    def __ge__(self, other):
        return self.pages >= other.pages

    def __eq__(self, other):
        return self.description == other.description

    def to_dict(self):
        return {'name': self.name,
                'description': self.description,
                'pages': self.pages,
                'author': self.author,
                'price': self.price}

    def __contains__(self, item):
        return item.lower() in self.name.lower()


class Library:

    def __init__(self):
        self.books = []

    def __len__(self):
        return len(self.books)

    def append(self, book):
        return self.books.append(book)

    def remove(self, book):
        return self.books.remove(book)

    def get_book(self):
        return {'Books': {obj.name: obj.pages for obj in self.books}}

    def find_the_biggest(self):
        fin = sorted(self.books, key=lambda b: getattr(b, 'pages'),
                     reverse=True)[0].name
        if len(self.books) == 0:
            return 'Your library is empty'
        return fin


book_1 = Book('Normal People', 'Very interesting book', 300,
              'Sally Rooney', '20$')
book_2 = Book('Conversations with friends', 'Not so interesting book',
              380, 'Sally Rooney', '40$')
book_3 = Book('Some book by Pushkin', 'Poetry', 100, 'Pushkin', '2$')
book_4 = Book('Some book', 'Poetry', 400, 'Pushkin', '1$')

print('normal' in book_1)

library = Library()
library.append(book_1)
library.append(book_2)
library.append(book_3)
library.append(book_4)
print(library.get_book())
library.remove(book_1)
print(library.get_book())
print(library.find_the_biggest())
print(len(library))
