
print("Welcome to the Calculator App")

def add(a,b):
    """ Add  two numbers and return the sum"""
    summation=round(a+b,4)
    print("The sum of",a," and ",b," is ",summation," . ")
    return str(a)+" + "+str(b)+" = "+str(summation)

def subtract(a,b):
    """ Subtract two numbers and return the difference """
    difference=round(a-b,4)
    print("The subtract of",a," and ",b," is ",difference," . ")
    return str(a)+" - "+str(b)+" = "+str(difference)

def multiply(a,b):
    """ Multiply two numbers and return the product"""
    product=round(a*b,4)
    print("The multiply of",a," and ",b," is ",product," . ")
    return str(a)+" * "+str(b)+" = "+str(product)

 
def devide(a,b):
    """Divide two numbers and return the quotient """
    #Perform the division if the denominator is not zero 
    if b!=0:
        quotient=round(a/b,4)
        print("The divide of",a," and ",b," is ",quotient ," . ")
        return str(a)+" / "+str(b)+" = "+str(quoyient)
    # Denominator is zero , result in error 
    else:
        print("You can not divide by zero ")
        return "DIV ERROR"


def exponent(a,b):
    """Take a number to power and return the result"""
    power=round(a**b,4)
    print("The exponent of",a," raised to the ",b," power is ",power," . ")
    return str(a)+" * "+str(b)+" = "+str(power)


# The main program

print("Welcome to the Python Calculator App")
print("Enter two numbers ")

history=[]
running=True



while running:
    # Get user input
    num1=float(input("\n Enter a number "))
    num2=float(input("Enter a number "))
    operator=input("Enter an operator (addition , subtraction,multiplication,division,or exponentiation, or a,s,m,d,e)").lower()

    #Call the appropriate function
    if operator=='addition' or operator=='a':
        result=add(num1,num2)
        
    elif operator=='subtraction' or operator=='s':
        result=subtract(num1,num2)
        
    elif operator=='multiplication' or operator=='m':
        result=multiply(num1,num2)
        
    elif operator =='division' or operator=='d':
        result=devide(num1,num2)
        
    elif operator=='exponentiation'or operator=='e':
        result=exponent(num1,num2)
    else:
        print("That is a not valid operation Try again")
        result="OPP ERROR"

# Append the mathematical result to the history
    history.append(result)

    #Allow user to quit

    choice=input("Would you like to run the program again (y/n):").lower()
    if choice!='y':
        print("\n Calculation Summary : ")
        for calc in history:
            print(calc)
        print("\nThank you for using Calculator App")
        running=False
























    
        































    





























    
