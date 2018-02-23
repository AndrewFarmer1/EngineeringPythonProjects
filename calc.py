#this code will take a user input and then will preform the desired operation using a GUI interface
import math 
from tkinter import *
from time import sleep
choice = None
selections = []
def calculateadd(self,event):
    for i in range(selections):
        ans = selections[i] + selections[i + 1]
        print (ans)
def calculatedivides(self,event):
    for i in range(selections):
        ans = selections[i] / selections[i + 1]
        print (ans)
def calculatemultiply(self,event):
    for i in range(selections):
        ans = selections[i] * selections[i + 1]
        print (ans)
def calculatesubtract(self,event):
    for i in range(selections):
      ans =  selections[i] - selections[i + 1]
      print (ans)
print ("Hello and welcome to my calculator program")
sleep(1)
print ("This program will take a predefined number of variables and will preform your desired operation.")
while choice == None:
    choice = float(input("Please enter the number of numbers you would like to use. Only use floats and intergers or else... >>> "))
    if type(choice) == int or type(choice) == float:
        for i in range(1,math.ceil(choice)+1):
            numbers = input("Please select your values you would like to use >>> ")
            selections.append(numbers)
            print (selections)
        print("Now lets pick our operation")
        sleep(5)
        window = Tk()
        topframe = Frame(window)
        topframe.pack(side=TOP)
        divide = Button(topframe, text="Divide", fg = "black")
        multiplication = Button(topframe, text="Multiply", fg = "black")
        addition = Button(topframe, text="Add", fg = "black")
        subtraction= Button(topframe, text="Subtract", fg = "black")
        divide.bind("<Button-1>",calculatedivides)
        multiplication.bind("<Button-1>",calculatemultiply)
        addition.bind("<Button-1>",calculateadd)
        subtraction.bind("<Button-1>",calculatesubtract)
        divide.pack()
        multiplication.pack()
        addition.pack()
        subtraction.pack()
        window.mainloop()
    else:
        print ("That is not a valid option please try again.")
        print(choice)
        choice = None

