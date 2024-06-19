import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    t = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="Shape", prompt="Pick a shape. A triangle, a square, or a circle.")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "Triangle" or shape == "triangle":
        t.color("black")
        t.pencolor("black")
        t.goto(0,0)
        t.circle(50,steps=3)
    elif shape == "Square" or shape == "square":
        t.color("black")
        t.pencolor("black")
        t.goto(0,0)
        t.circle(50,steps=4)
    else:
        if shape == "Circle" or shape == "circle":
            t.color("black")
            t.pencolor("black")
            t.goto(0,0)
            t.circle(50,steps=200)
    # Call the turtle .done() method
    turtle.done()