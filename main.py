import elements
import random                 # To import random module for making random choice for the computer
import click                  # For clearing the screen after every game 
def clrscr():
                              # Clear screen using click.clear() function
    click.clear()
print(elements.welcome_element)       # To import game Heading from elements.py
play="Y"
while play=="Y" or play=="y": # The Game will keep running until this while statement breaks
  choice=int(input("Enter Your Choose:\nType 0 for Rock , 1 for Paper , 2 for scissors:\n)> "))
  if choice==0 or choice==1 or choice==2:
    print("Your choice:")
    if choice==0:
      print(elements.rock_element)
    elif choice==1:
      print(elements.paper_element)
    elif choice==2:
      print(elements.scissors_element)
    else:
      print("Kindly enter an Valid Number 0 , 1 , 2 only")  # Checks if the input was valid 
    print("Computer's choice :")
    choice_computer=random.randint(0,2)  # Random Function to make a random choice between 0,1,2             
    if choice_computer==0:
      print(elements.rock_element)
    elif choice_computer==1:
      print(elements.paper_element)
    elif choice_computer==2:
      print(elements.scissors_element)
    string_choice=str(choice)
    string_choice_computer=str(choice_computer)
    num=string_choice+string_choice_computer
    if num=="02"or num=="10"or num=="21":       # Checks the numbers to see if you've won 
      print("You Won :) , Have a lucky Day Ahead")
    elif num=="00"or num=="11" or num=="22":
        print("It's a Tie :| , You are a Tough Opponent")
    else:
      print("You lost. Better luck next time ")
  else:
    print("Please Enter a valid number 0 , 1 , 2 .")
  print("\r")
  play=input("Do you want to play again.\nIf Yes then type : 'Y' , if u want to exit type 'N':\n)> ")
  clrscr()                                                            # input to breaking the while loop
print("\r")
print("Thanks For Playing , Come Back Soon :)")
# Rock Paper Scissors Version 3.0
# Created By Alex Tomsovic
# Feel free to recreate / implement with this code
