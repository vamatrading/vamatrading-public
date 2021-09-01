#this may be more complicated than it needs to be, but I wanted to be able to perform simple mathmatical
#operations using a dictionary and input if at all possible

from math import *

def function_creator():
    
    expr = input("Enter the simple arithmetic equation(in terms of x & y): ")
    
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    z = eval(expr)
    print("z = {}".format(z))
    


#adict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10}

#w = input("What operation would you like to perform: Add, Subtract, Multiply, or Divide? ")

#a,b = input("Please enter two numbers between 1 - 10, spelling out the word for each number:  ").split()



