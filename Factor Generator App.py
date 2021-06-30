print("Generate Factor App")
print("Welcome to the Factor Generate App ")

running=True
#Run the program until the user quits

while running:
    #Get user input
    number=int(input("\n Enter a number to determine all factors of that numbers "))
    #find the factors of the users given number

    factors=[]
    for  i in range(1,number+1):
        if number%i==0:
            factors.append(i)
            
    print("\n Factors of ",number," are ")
    for factor in factors:
        print(factor)
    # summy of teh fators mathematically
    
    for  i in range(int(len(factors)/2)):
        print(factors[i],"*",factors[-i-1]," = ",number)
        
        # ask the user if would like to quit

    choice=input("\n Running again (y/n) : ").lower()
    if choice!='y':
        running=False
        print("Thank you for using Program Have a god Day !!! ")
