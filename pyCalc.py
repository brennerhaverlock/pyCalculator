# added operations

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exp(x, y):
    return x ** y


# user input

print("Pick an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Raise a power")


choice = input("Enter choice: ")

first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))

if choice == '1':
    print(first_num, "+", second_num, "=", add(first_num, second_num))
elif choice == '2':
    print(first_num, "-", second_num, "=", subtract(first_num, second_num))
elif choice == '3':
    print(first_num, "*", second_num, "=", multiply(first_num, second_num))
elif choice == '4':
    print(first_num, "/", second_num, divide(first_num, second_num))
elif choice == '5':
    print(first_num, '**', second_num, '=', exp(first_num, second_num))
else:
    print("Please pick a valid input number/operation")
