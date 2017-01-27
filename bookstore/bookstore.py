class Bookstore(object):
    
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def get_books(self):
        return self.books
    
    def add_book(self, Book):
        self.books.append(Book)

    def search_books(self, title = None, author = None):
        booklist = []
        if title:
            for book in self.books:
                if title.lower() in book.title.lower():
                    booklist.append(book)
            return booklist
        elif author:
            for book in self.books:
                if book.author == author:
                    booklist.append(book)
            return booklist
        elif title and author:
            for book in self.books:
                if book.title == title and book.author == author:
                    booklist.append(book)
            return booklist
        else: 
            raise ValueError('No title or author given.')

class Author(object):
    
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    
    def get_books(self):
        return self.books
    
    def add_book(self, Book):
        self.books.append(Book)

class Book(object):
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.author.add_book(self)
        
'''
melville = Author('Herman Melville', 'US')
melville.name
>>>"Herman Melville"

moby = Book("Moby Dick", author=melville)
moby.title
>>>"Moby Dick"
moby.author.name
>>>"Herman Melville"
store.add_book(moby)
'''

store = Bookstore("Rmotr's bookstore")
borges = Author("Jorge Luis Borges", "AR")
poe = Author('Edgar Allan Poe', 'US')

ficciones = Book("Ficciones", author=borges)
aleph = Book("The Aleph", author=borges)
raven = Book("The Raven", author=poe)
store.add_book(ficciones)
store.add_book(aleph)
results = store.search_books(title='ficc')
print results