"""
Day 12: Polymorphism & Special Methods
Date: February 27, 2026
Description: Magic methods and operator overloading
"""

# Example 1: Polymorphism
print("="*50)
print("EXAMPLE 1: Polymorphism")
print("="*50)

class Dog:
    def speak(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

class Fish:
    def speak(self):
        return "Blub blub"
    
    def move(self):
        return "Swimming in water"

class Bird:
    def speak(self):
        return "Tweet tweet"
    
    def move(self):
        return "Flying in the sky"

# Polymorphism - same method names, different behaviors
def animal_info(animal):
    """Works with ANY object that has speak() and move() methods"""
    print(f"Sound: {animal.speak()}")
    print(f"Movement: {animal.move()}")
    print()

# Test
dog = Dog()
fish = Fish()
bird = Bird()

animal_info(dog)
animal_info(fish)
animal_info(bird)


# Example 2: __str__ and __repr__
print("="*50)
print("EXAMPLE 2: String Representations")
print("="*50)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """For end users - readable"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """For developers - recreatable"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

book = Book("Python Basics", "John Doe", 300)

# __str__ is used by print()
print(book)
# Output: 'Python Basics' by John Doe

# __repr__ is used in console/lists
print(repr(book))
# Output: Book('Python Basics', 'John Doe', 300)

# In a list, __repr__ is used
books = [book]
print(books)

# Example 3: __len__
print("\n" + "="*50)
print("EXAMPLE 3: __len__ Method")
print("="*50)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __len__(self):
        """Makes len(playlist) work!"""
        return len(self.songs)
    
    def __str__(self):
        return f"Playlist '{self.name}' with {len(self)} songs"

# Test
playlist = Playlist("My Favorites")
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

# Now len() works on our custom class!
print(f"Number of songs: {len(playlist)}")
print(playlist)


# Example 4: Comparison Operators
print("\n" + "="*50)
print("EXAMPLE 4: Comparison Magic Methods")
print("="*50)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        """Equal to (==)"""
        return self.grade == other.grade
    
    def __lt__(self, other):
        """Less than (<)"""
        return self.grade < other.grade
    
    def __gt__(self, other):
        """Greater than (>)"""
        return self.grade > other.grade
    
    def __str__(self):
        return f"{self.name}: {self.grade}"

# Test
alice = Student("Alice", 90)
bob = Student("Bob", 85)
charlie = Student("Charlie", 90)

print(f"Alice == Charlie? {alice == charlie}")  # True (same grade)
print(f"Bob < Alice? {bob < alice}")  # True (85 < 90)
print(f"Alice > Bob? {alice > bob}")  # True (90 > 85)

# Can even sort a list of students!
students = [alice, bob, charlie]
students.sort()  # Uses __lt__ for sorting
print("\nSorted by grade:")
for student in students:
    print(student)


# Example 5: Arithmetic Operators
print("\n" + "="*50)
print("EXAMPLE 5: Arithmetic Magic Methods")
print("="*50)

class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, other):
        """Addition (+)"""
        return Money(self.amount + other.amount)
    
    def __sub__(self, other):
        """Subtraction (-)"""
        return Money(self.amount - other.amount)
    
    def __mul__(self, multiplier):
        """Multiplication (*)"""
        return Money(self.amount * multiplier)
    
    def __str__(self):
        return f"${self.amount:.2f}"

# Test
wallet1 = Money(100)
wallet2 = Money(50)

# Now we can use + - * on our custom class!
total = wallet1 + wallet2
print(f"Wallet1 + Wallet2 = {total}")

difference = wallet1 - wallet2
print(f"Wallet1 - Wallet2 = {difference}")

doubled = wallet1 * 2
print(f"Wallet1 * 2 = {doubled}")

# Example 6: Context Manager (__enter__ and __exit__)
print("\n" + "="*50)
print("EXAMPLE 6: Context Manager (Bonus)")
print("="*50)

class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        if self.file:
            print(f"Closing {self.filename}")
            self.file.close()

# Usage - just like with open()!
with FileManager('test.txt') as f:
    f.write("Hello World!")
    print("File is open and being written to")


print("File is now closed")