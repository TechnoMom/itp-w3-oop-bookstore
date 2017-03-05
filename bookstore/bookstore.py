class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []


# Show the books in the bookstore
    def get_books(self):
        return self.books


# Add a book to the bookstore
    def add_book(self, book):
        self.books.append(book)


# Search for books by author and/or title
    def search_books(self, title=None, author=None):
        answer = []
        for book in self.books:
            if title != None:
                if title.lower() in book.title.lower():
                    answer.append(book)
            elif author != None:
               if author == book.author:
                    answer.append(book)
            elif author != None and title != None:
                if author == book.author and title.lower() in book.title.lower():
                    answer.append(book)
        return answer                    

    
        
class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = [] 


# Add in books
    def add_book(self, book):
        self.books.append(book)


# Search for books
    def get_books(self):
        return self.books


        
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
# Add books to the Author's list
        self.author.add_book(self)