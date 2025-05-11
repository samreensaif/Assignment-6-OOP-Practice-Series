
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Creating an instance of Multiplier
multiplier = Multiplier(5)

# Using callable() to check if the object is callable
print(callable(multiplier))  # Output: True

# Calling the object like a function
result = multiplier(10)
print(result)  # Output: 50
