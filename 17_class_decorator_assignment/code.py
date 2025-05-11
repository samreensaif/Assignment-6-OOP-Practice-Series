
# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the greet method to the class
    cls.greet = greet
    return cls

# Applying the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Creating an instance of the decorated Person class
person1 = Person("Alice")

# Calling the greet method
print(person1.greet())  # Output: Hello from Decorator!
