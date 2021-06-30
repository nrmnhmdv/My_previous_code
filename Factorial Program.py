import math
print("Welcome to the Factorial Calculator App")

number =int(input("What number would you like to compute the factorial of "))
print("What is factorial ")

print(str(number)+"! = ",end="")
for i in range(1,number):
    print(str(i),end="*")
print(str(number))
print()

print("Here is the result from the math library : ")
print("The factorial of ",number," is ",math.factorial(number))

print("Here is the result from my own algorithm : ")

fac=1
for i in range(1,number+1):
    fac=fac*i
print("The factorial of",number ,"is",fac)


    
