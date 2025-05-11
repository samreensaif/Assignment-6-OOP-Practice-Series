
class Book:
    # Class variable to keep track of the total number of books
    total_books = 0

    def __init__(self, title, author):
        self.title = title  # Instance variable for book title
        self.author = author  # Instance variable for book author
        Book.increment_book_count()  # Call the class method to increment the book count when a new book is added

    @classmethod
    def increment_book_count(cls):
        # Increment the total_books class variable
        cls.total_books += 1

# Example usage:
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book4 = Book("Pride and Prejudice", "Jane Austen")

# Print the total number of books
print(f"Total books: {Book.total_books}")  # Output: Total books: 3
