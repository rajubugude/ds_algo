class Library:
    _total_books = 100  # Class variable to track total books (shared across all instances)

    def __init__(self, lib_name):
        self.lib_name = lib_name  # Instance variable for library name

    @classmethod
    def get_total_books(cls):
        # Class method: Accesses class-level state
        return cls._total_books

    @classmethod
    def add_books(cls, count):
        # Class method: Modifies class-level state
        cls._total_books += count
        return cls._total_books

    @staticmethod
    def is_valid_isbn(isbn):
        # Static method: Utility function, no access to cls or self
        # Simple ISBN validation (e.g., checks if it's a 10-digit string)
        return isinstance(isbn, str) and len(isbn) == 10 and isbn.isdigit()


# Test the methods
print(Library.get_total_books())  # Output: 100
Library.add_books(50)
print(Library.get_total_books())  # Output: 150

print(Library.is_valid_isbn("1234567890"))  # Output: True
print(Library.is_valid_isbn("12345abcde"))  # Output: False
print(Library.is_valid_isbn("12345"))       # Output: False

# Test with an instance
library = Library("City Library")
print(library.get_total_books())  # Output: 150 (class method works with instance)
print(library.add_books(25))       # Output: 175 (updates shared total)
print(library.is_valid_isbn("0987654321"))  # Output: True (static method works with instance)