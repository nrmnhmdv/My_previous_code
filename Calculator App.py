from builtins import float, input, int

print("Welcome to the Calculator App My Own Algorithm")
print("Enter two numbers and an operation and the desired operation will be performed")


def addition(number1,number2):
    a=float(number1+number2)
    return a

def subtraction(number1,number2):
    b=float(number1-number2)
    return b

def multiplication(number1,number2):
    c=float(number1*number2)
    return c


def division(number1,number2):
    if number2>0:
        d=float(number1/number2)
        return d
    elif number2==0:
        return "You can not divide by zero "

def exponentiation(number1,number2):
        return float(number1**number2)



running=True

while running:
    number1=int(input("Enter a number : "))
    number2=int(input("Enter a number : "))
    operation=input("Enter an operation(addition,subtraction,multiplication,division, exponentiation)").strip()

    if operation=='addition':
        print("Addition is ",addition(number1,number2))
    elif operation=='subtraction':
        print(subtraction(number1,number2))
    elif operation=='multiplication':
        print(multiplication(number1,number2))
    elif operation=='division':
        print(division(number1,number2))
    elif operation=='exponentiation':
        print( exponentiation(number1,number2))



    choice = input("Would you like to run the program again (y/n): ").lower()

    if choice!='y':
        print("Thank you for using Calculator app")
        running=False
   















    
