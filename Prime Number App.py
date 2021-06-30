import time
print("Welcome to the Prime App ")

running=True
# Run the program as long as the user wants

while running:
    #Get user input
    print("\n Enter 1 to determine if a specific number is prime ")
    print("\nEnter 2 to determine  all prime numbers within a set range")
    option=input("Enter your choice 1 or 2 : ")
    # Determine if a single number is prime

    if option=='1':
        number=int(input("\n Enter a number to determine if it is prime or not "))

        #Prime status check
        prime_status=True
        for i in range(1,number+1):
            
            if number%i==0:
                prime_status=False
                break
        #print summary
        if prime_status:
            print(number," is prime ")
        else:
            print(number," is not prime")

    # Determine primes within a range values  and the time

    elif option=='2':
        l_bound=int(input("\nEnter the lower bound of your range "))
        u_bound=int(input("\nEnter the upper bound of your range "))

        primes=[]
        #Get the current time 
        start_time=time.time()
        #Check prime status of all numbers
        for prime_candidate in range(l_bound,u_bound+1):
            # 1 is not prime
            if prime_candidate>1:
                prime_status=True
                for i in range(2,prime_candidate):
                    if prime_candidate%i==0:
                        prime_status=False
                        break
            else:
                prime_status=False

            # prime canddiate is in fact prime !            
            if prime_status:
                primes.append(prime_candidate)
        #print(primes)

# get the current time
        end_time=time.time()

        delta_time=round(end_time-start_time,4)
        print("Calculations took a total of ",delta_time)
        #print("")
        for prime in primes:
            print(prime)

    choice=input("Enter a choice (y/n) ")

    if choice!='y':
        running=False




















        






















        

        
        
