"""
Day 12: Polymorphism & Special Methods - Exercise.
Date: March 1, 2026
Description: 2D Vector, 
"""
import math

print("="*50)
print("Exercise 1 - 2D Vector.")
print("="*50)

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"
    
    def __repr__(self):
        return f"Vector2D({self.x},{self.y})"
    
    def __add__(self, other):
        """Adding two vectors."""
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Vector2D(new_x , new_y)
    
    def __sub__(self, other):
        """Subtracting two vectors."""
        new_x = self.x - other.x
        new_y = self.y - other.y

        return Vector2D(new_x , new_y)
    
    def __mul__(self, scalar):
        """Multiplying vector with the number."""
        new_x = self.x * scalar
        new_y = self.y * scalar

        return Vector2D(new_x,new_y)
    
    def __eq__(self, other):
        """Checking the two vectors are equal or not."""
        return self.x == other.x and self.y == other.y
    
    def __abs__(self):
        """Getting length or magnitude of the vector."""
        length = math.sqrt(self.x**2 + self.y**2)
        return length
    

if __name__ == "__main__":
    v1 = Vector2D(3,4)
    v2 = Vector2D(1,2)
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1+v2}")
    print(f"v1 - v2 = {v1-v2}")
    print(f"v1 * 2 = {v1*2}")
    print(f"v1 == v2 = {v1==v2}")
    print(f"|v1| = {abs(v1)}")


print("="*50)
print("Exercise 2 - Book & Library.")
print("="*50)

class Book:
    def __init__(self,title, author, pages, year):
        self.title = title
        self.author = author 
        self.pages = pages
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}','{self.pages}','{self.year}')"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages


class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def remove_book(self,book):
        self.books.remove(book)
        print(f"Removed: {book.title}")

    def __str__(self):
        return f"{self.name} ({len(self.books)} books)"
    
    def __len__(self):
        return len(self.books)
    
    def __getitem__(self, index):
        return self.books[index]
    
    def __contains__(self, book):
        return book in self.books
    
    def __iter__(self):
        return iter(self.books)
    

    
if __name__ == "__main__":

    book1 = Book("Python Basics","John Doe",300,2020)
    book2 = Book("Advanced Python","Jane Smith",450,2021)
    library = Library("City Library")
    library.add_book(book1)
    library.add_book(book2)
    print(len(library))
    print(len(library))
    print(library[0])
    print(book1 in library)
    for book in library:
        print(book)
    

    