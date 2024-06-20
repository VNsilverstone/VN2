"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""


numbers = input("Enter a number.")
numbers2 = input("Enter a second number.")
calculate = input("Do you want to add, subtract,multiply, or divide your numbers.")

if calculate == "add" or calculate  == "Add":
    print("The sum of your numbers is " + str(int(numbers) + int(numbers2)))
else:
    if calculate == "subtract" or calculate == "Subtract":
        print("The answer when subtracting your numbers is " + str(int(numbers) - int(numbers2)))
    elif calculate == "multiply" or calculate == "Multiply":
        print("The product of your numbers is " + str(int(numbers) * int(numbers2)))
    elif calculate == "divide" or calculate == "Divide":
        print("The divident of uour numbers is " + str(int(numbers) / int(numbers2)))