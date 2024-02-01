# <Graysen Schwaller>             <09/12/2023>
# <Lucky Calculator / Lab section 6 / Class Section J>
# <A multi-faceted function that can execute calculations & pseudo random number generation>
import random as rand

# NOTE: Function definitions should go here!

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def truediv(x,y):
    return x/y
def floordiv(x,y):
    return x//y
def mod(x,y):
    return x%y
def pow(x,y):
    return x**y

# def takeInt():
#     theNumberTheyAreInFactInputtingAtTheCurrentMomentInTime = int(input("Input a number for the operation "))
#     return theNumberTheyAreInFactInputtingAtTheCurrentMomentInTime

def takeInt(whichOperand, Zero): 
    theNumberTheyAreInFactInputtingAtTheCurrentMomentInTime = int(input("Input a number for the operation "))
    theSecondNumberTheyAreInFactInputtingAtTheCurrentMomentInTime = int(input("Input a number for the operation "))
    if Zero & (whichOperand == 2) & (theNumberTheyAreInFactInputtingAtTheCurrentMomentInTime == 0):
        print("Oh my god bro, you trying to mess up my program?")
        print("ERROR: Divide by 0: substituted 1 for 0")
        theNumberTheyAreInFactInputtingAtTheCurrentMomentInTime = 1
    return theNumberTheyAreInFactInputtingAtTheCurrentMomentInTime, theSecondNumberTheyAreInFactInputtingAtTheCurrentMomentInTime

def calculator():
    op_list = {"+":add, '-':sub, '*':mul, '/':truediv, '//':floordiv, '%':mod, '**':pow}
    while(True):
        operator = input("Choose an operator; '+', '-', '*', '/', '//', '%', or '**': ")
        if((operator == "+") | (operator == "-")| (operator == "*")| (operator == "/")| (operator == "//")| (operator == "%")| (operator == "**")):
            break
        print("Something don't seem right there, please try again")
    divideZero = (operator == "/") | (operator == "//") | (operator == "%")
    num1, num2 = takeInt(1, divideZero)
    return (op_list[operator](num1,num2))
    

def luckyNumber(): 
    ret = 0
    a,b = takeInt(0,False) 
    if(a < b):
        lukNum = rand.random()*b + a
    else:
        lukNum = rand.random()*a + b
    ret = lukNum
    return ret
    
def quitMaybe(byebye):
    if byebye == "q":
        print("So long-a Bowser!")
        print("Maybe next time you'll actually wanna have fun")
        quit()
    else:
        print("I don't understand what you're trying, try again, bud")
        clq()

def clq():
    choice = input("[c]alculator, [l]ucky number, [q]uit: ")
    if choice == "c":
        calcuNum = calculator()
        print("The end result of your ardous calculations is: {0}".format(calcuNum))
    elif choice == "l":
        lukNum = luckyNumber()
        print("Your lucky number is the absolutely gobsmacking number of {0}".format(lukNum))
    else:
        print(quitMaybe(choice))

print("Lucky Calculator!")
print()

print("By: Graysen Schwaller")
print("[COM S 127 J]")
print()

# Determine initial player choice
print("What would you like to do?")
print()
clq() 
print()

# initial choice tasks (1 pt.) ----------------------------------------------------------------------------------------------------------------
# DONE: Use conditional logic to determine which function of the Lucky Calculator to use: [c]alculator, [l]ucky number, [q]uit
#       - Create a section of code that executes if the user enters 'c' as their initial choice instead of 'l' or 'q'.
#       - Create a section of code that executes if the user enters 'l' as their initial choice instead of 'c' or 'q'.
#       - Create a section of code that executes if the user enters 'q' as their initial choice instead of 'c' or 'l'.
# DONE: Add another section of code where if the user does not enter 'c', 'l', or 'q' in their initial choice, the script will print out an 
#       error message stating: 
#       print("ERROR: I did not understand your input... Please try again...") or something similar (use your imagination).
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'c' option tasks (3 pts.) -------------------------------------------------------------------------------------------------------------------
# DONE: Inside the 'c' option, take in input from the user for one of seven calculations: [+], [-], [*], [/], [//], [%], [**]
# DONE: Depending on the input from the calculation choice step above, use conditional logic to determine which calculation to perform.
# DONE: If the user does not enter '+', '-', '*', '/', '//', '%', or '**' in their calculation choice, print out an error message stating: 
#       print("ERROR: You must enter either \"+\", \"-\", \"*\", \"/\", \"//\", \"%\", or \"**\"") or something similar (use your imagination).
# DONE: Program a function that takes in input for the left and right hand terms of the chosen operation, converts this input to the integer 
#       type, and then returns these two integer values. Use a generic prompt for the input such as: input("Please Enter An Integer: ")
#
#       NOTE: You MUST program a function for this - do not just take the user's input 'in line.'
#
# DONE: In each condition for each type of calculation, call then previously created input function, and return both values to variables.
# DONE?: Program a function for each calculation type which takes parameters for the left hand side and right hand side of the operator.
#
#       NOTE: You MUST program functions for this - do not just perform the calculations 'in line.'
#
# DONE: For your '/', '//', and '%' functions, use conditional logic to check if the right hand side of the expression is zero (0) and print an error 
#       if it is. In this case, change the right hand side term from zero (0) to one (1), and perform the operation as it would normally be done.
# DONE: Pass in the left/ right term variables, found earlier, as arguments to each function, perform the calculation, then returns the 
#       result to a new variable.
# DONE: Print the contents of the variable that was assigned the value of your function return with a message like:
#       print("The result of your calculation was: {0}".format(answer))
#       (use your imagination).
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'l' option tasks (1 pt.) --------------------------------------------------------------------------------------------------------------------
# DONE: Call the input function created in the 'c' option tasks, and return its output to a pair of variables.
# DONE: Create a new function, called 'luckyNumber,' which takes the two previous variables, here called 'a' and 'b', as input.
# DONE: Assign the output of the 'luckyNumber' function to a variable.
# DONE: Inside the luckyNumber function, initialize a 'return value variable' to zero (0).
# DONE: After the 'return value variable,' implement the following conditional logic:
#       - if 'a' is less than 'b,' assign a random value between the range of 'a' and 'b + 1' to the 'return value variable'
#       - else, return a random value between the range of 'b' and 'a + 1' to the 'return value variable'
# DONE: Once the 'return value variable' has been assigned its value, return it at the end of the function.
# DONE: Back inside the 'l' section of the code, after the 'luckyNumber' function has been called and has returned its value,
#       print a fun message to the user with their 'lucky number,' such as: print("Your lucky number is: {0}".format(answer))
#       (use your imagination).
# ---------------------------------------------------------------------------------------------------------------------------------------------
