class Employee:
    def __init__(self, name, position, salary):
        # Initializing the attributes
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        # Method to increase the salary by a given amount
        self.salary += amount

    def display_employee(self):
        # Method to display employee details
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary:  ₱ {self.salary}")

# Creating an employee
employee1 = Employee("Ivy Gersola", "Sales Assistant Head", 5000)

# Giving a raise
employee1.give_raise(3125)

# Displaying employee details
employee1.display_employee()
