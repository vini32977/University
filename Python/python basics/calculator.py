from random import choice


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

while True:
    print("ARITHMETIC OPERATIONS")
    print("*********************")
    print("1.TO PERFORM ADDITION")
    print("2.TO PERFORM SUBTRACTION")
    print("3.TO PERFORM MULTIPLICATION")
    print("4.TO PERFORM DIVISION")
    choice=int(input("Enter your choice"))
    if choice==5:
        print("EXITING THE PROGRAM")
        break

    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))

    if choice==1:
        result=add(num1,num2)
        print("Result: ",result)
    elif choice == 2:
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == 3:
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == 4:
        result = divide(num1, num2)
        print("Result: ", result)
    else:
        print("Invalid option")

