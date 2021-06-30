import cmath
#Print Welcome Information
print("Quadratic Equation Solver App")
print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion")

#Get user input
equastions=int(input("How many equations would you like to solve today:"))

# Loop through and solve each equation
for i in range(equastions):
    print(" Solving equation "+str(i+1))

    print("---------------------------------------------")
    a=float(input("Please enter your value of x^2 "))
    b=float(input("Please enter your value of x  "))
    c=float(input("Please enter your value of c  "))

#Solving the quadratic formula 
    x1=(-b+cmath.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-cmath.sqrt(b**2-4*a*c))/(2*a)

    print("The solution to ",a,'x^2',"+",b,'x',"+",c,"=","0")
    print("\n\tx1 = " + str(x1))
    print("\tx2 = " + str(x2))

print("\nThank you for using the Quadratic Equation Solver App. Goodbye.")
print("!!!!!!!!!!! THANK YOU SO MUCH !!!!!!!!!!!!!!!!!!")
