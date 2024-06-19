# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import math

Ask1 = input("Enter a radius for a circle")
Ask2 = input("Do you want to find the area or the circumference of the circle that you entered the radius of?")
if Ask2 == "Area" or Ask2 == "area":
    print( math.pow(int( math.pi * int(Ask1)), 2))
elif Ask2 == "Circumference" or Ask2 == "circumference":
    print(int(2 * math.pi * int(Ask1)))
#Area = πr^2
#Circumference = 2πr