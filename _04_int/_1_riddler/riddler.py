"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
score = 0
Riddle1 = input(" What goes up but never comes down?")
Riddle2 = input("I start with the letter e,end with the letter e,I am one letter and I am not the letter e!What am I?")
Riddle3 = input("Why did the chicken cross the road")
if Riddle1 == "Age" or Riddle1 == "age":
    score = score + 1

if Riddle2 == "An Envelope" or  Riddle2 == "an envelope" or Riddle2 == "A envelope" or Riddle2 == "a envelope":
            score = score + 1

if Riddle3 == "To get to the other side" or Riddle3 == "to get to the other side":
                score = score + 1

print(" You got " + str(score) + " questions correct.")
