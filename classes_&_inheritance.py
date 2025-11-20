# Q1
# class Employee:
#     def __init__(self, n, d, s):
#         self.name = n
#         self.department = d
#         self.salary = s

#     def display_info(self):
#         print("\nEmployee Information:")
#         print(f"Name: {self.name}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")

# name = input("Enter employee name: ")
# department = input("Enter department: ")
# salary = float(input("Enter salary: "))

# emp = Employee(name, department, salary)

# emp.display_info()

# Q2
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print("\nStudent Information:")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# class Student(Person):
#     def __init__(self, name, age, student_id, grade):
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.grade = grade

#     def display_student_info(self):
#         self.display_info()
#         print(f"Student ID: {self.student_id}")
#         print(f"Grade: {self.grade}")

# name = input("Enter student name: ")
# age = int(input("Enter student age: "))
# student_id = input("Enter student ID: ")
# grade = input("Enter student grade: ")

# student = Student(name, age, student_id, grade)

# student.display_student_info()

# Q3
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_person_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# class Employee:
#     def __init__(self, employee_id, salary):
#         self.employee_id = employee_id
#         self.salary = salary

#     def display_employee_info(self):
#         print(f"Employee ID: {self.employee_id}")
#         print(f"Salary: {self.salary}")

# class Manager(Person, Employee):
#     def __init__(self, name, age, employee_id, salary, department):
#         Person.__init__(self, name, age)
#         Employee.__init__(self, employee_id, salary)
#         self.department = department

#     def display_manager_info(self):
#         self.display_person_info()
#         self.display_employee_info()
#         print(f"Department: {self.department}")

# name = input("Enter manager name: ")
# age = int(input("Enter age: "))
# employee_id = input("Enter employee ID: ")
# salary = float(input("Enter salary: "))
# department = input("Enter department: ")

# manager = Manager(name, age, employee_id, salary, department)

# print("\nManager Information:")
# manager.display_manager_info()