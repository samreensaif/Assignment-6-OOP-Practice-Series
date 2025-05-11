
class Employee:
    # Public variable
    name = "John Doe"

    # Protected variable
    _salary = 50000

    # Private variable
    __ssn = "123-45-6789"

    def display_info(self):
        # Method to display all variables
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")


# Creating an object of Employee
emp = Employee()

# Accessing public variable
print(emp.name)  # Output: John Doe

# Accessing protected variable
print(emp._salary)  # Output: 50000

# Accessing private variable
# This will raise an error since it's private
# print(emp.__ssn)  # Uncommenting this will cause an AttributeError
emp.display_info()


