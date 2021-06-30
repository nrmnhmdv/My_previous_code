print("Welcome to the Even odd Number Sorter App  My own Algorithm ")

running=True
evens=[]
odds=[]
#count_even=0
#count_dd=0
while running:
    n=int(input("Please enter number for for loop "))
    list_sort=[]
    for i in range(n):
        number=int(input("Please enter a number "))
        list_sort.append(number)
        
    print("---- Result Summary --------")
    for number in list_sort:
        if number%2==0:
            evens.append(number)
            #count_even+=1
            print("\t",number," is even ")
        else:
            odds.append(number)
            #count_odd+=1
            print("\t",number," is odd ")
        evens.sort()
        odds.sort()

    print("The numbers are even : ")
    for even in evens:
        print(even)

    print("The numbrs are odd : ")
    for odd in odds:
        print(odd)

    choice=input("Would you like to run the program again ? (y/n ) : " ).lower()
    if choice!='y':
        running=False
