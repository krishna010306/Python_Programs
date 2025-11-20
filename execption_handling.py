# Q1
# try:
#     numerator = int(input("Enter numerator: "))
#     denominator = int(input("Enter denominator: "))
#     result = numerator / denominator
#     print(f"Result: {result}")

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed!")

# except ValueError:
#     print("Error: Please enter valid integers!")

# finally:
#     print("Execution completed.")

# Q2
# class InvalidPasswordException(Exception):
#     pass

# def check_password(password):
#     correct_password = "Python@123"
#     if password != correct_password:
#         raise InvalidPasswordException("Incorrect password!")
#     print("Access granted! Password is correct.")

# try:
#     password = input("Enter your password: ")
#     check_password(password)
# except InvalidPasswordException as e:
#     print(e)
