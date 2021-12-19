from art import logo
from operations import math_operations

print(logo)
# continue_math = True
num1 = int(input("what is the first number\n>"))
while(True):

    operation = input(
        "what operation would you like to perform\n + - / X\n>")
    num2 = int(input("what is the second number\n>"))
    print(
        f"{num1} {operation} {num2} = {math_operations[operation](num1,num2)}")

    if(input("would you like to continue with the result\n>").lower() == "n"):
        num1 = int(input("what is the first number\n>"))
    else:
        num1 = math_operations[operation](num1, num2)
