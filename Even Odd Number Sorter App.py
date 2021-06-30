print("Welcome to the Even Odd OSrter App")
running=True

while running:
    num_string=input("Enter in a string of numbers seperated by a coma (,) : ")
    
    num_string=num_string.replace(' ','')
    num_list=num_string.split(",")

    #initialize lists to hold even/odd values 
    evens=[]
    odds=[]

    #Calculate whether the number is evem or odd
    print("\t Summary ")
    for number in num_list:
        number=int(number)
        if number%2==0:
            evens.append(number)
            print(number," Is even !!! ")
   
        else:
            print(number , " Is odd !!! ")
            odds.append(number)
        evens.sort()
        odds.sort()
        
    print("The even numbers  are :")
    for even in evens:
        print(even)

    print("The odd numbers  are :")
    for  odd in odds:
        print(odd)
    choice=input("Would you like to running the app again ? (y/n ) :").lower()
    if choice!='y':
        running=False
        print("Thank you for using My Program !!! ")
