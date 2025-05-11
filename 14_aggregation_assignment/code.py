
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_employee_info(self):
        return f"{self.name} is a {self.position}"

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store employees in the department

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def show_department_info(self):
        print(f"Department: {self.department_name}")
        for employee in self.employees:
            print(employee.get_employee_info())

# Example usage:
emp1 = Employee("Alice", "Manager")
emp2 = Employee("Bob", "Developer")
emp3 = Employee("Charlie", "Designer")

# Create a Department object and add employees to it
department = Department("IT")
department.add_employee(emp1)
department.add_employee(emp2)
department.add_employee(emp3)

# Display department and employees information
department.show_department_info()
