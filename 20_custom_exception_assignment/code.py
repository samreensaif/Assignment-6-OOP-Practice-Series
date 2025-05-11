
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is not valid, must be 18 or older.")
    return f"Age {age} is valid."

# Testing the custom exception
try:
    age = 16
    print(check_age(age))  # This will raise InvalidAgeError
except InvalidAgeError as e:
    print(f"Error: {e}")  # Output: Error: Age 16 is not valid, must be 18 or older.
