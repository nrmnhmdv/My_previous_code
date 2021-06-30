import math
print("Wellcome to the Multible Table")
Say_name=input("What is your name? ")
print("Hello ! "+Say_name.title())
number=float(input("Please enter the number for the Multible Table "))

print(" Multiplication Table For : "+str(number))
for i in range(1,11):
 c=i*number
 print(str(i)+"*"+str(number)+"="+str(c))


print("-----------------------------")

print(" Exponent Table  ")
for i in range(1,11):
    c=i*number
    print(str(number)+"*"+str(i)+"="+str(c))

message=Say_name.title()+" Math is cool"

print('\n',message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())


    
    
