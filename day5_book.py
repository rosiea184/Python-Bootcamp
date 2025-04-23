class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, File Size: {self.file_size}MB")

book1 = Book("To Kill a Mockingbird", "Harper Lee")
book1.display_info()

ebook1 = Ebook("Python Programming", "John Doe", 2)
ebook1.display_info()