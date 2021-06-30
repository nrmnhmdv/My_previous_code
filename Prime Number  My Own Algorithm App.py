print("Welcome to the welcome to the prime app")
# what is prime number

cout_prime=0
running=True
count_prime2=0

print("Enter 1 to determine if a specific number is prime.")
print("Enter 2 to determine all prime numbers within a set range. ")



while running:

    number=int(input("Enter our choice 1 or 2 : "))

    if number==1:
        n=int(input("Enter a number to determine if t is prime or not "))
        for i in range(1,n+1):
            c=n%i
            if c==0:
                cout_prime+=1
    
        if cout_prime==2:
            print("It is prime ")
        else:
            print("It is not prime ")


    elif number==2:
        lower_bound=int(input("Enter lower bund of your range :"))
        upper_bound=int(input("Enter upper bound of your range : "))

        for prime_candidate in range (lower_bound,upper_bound+1):

             if prime_candidate >1:

                for i in range (2,prime_candidate):
                    
                    if prime_candidate%i==0:
                        break
                else:
                    print(prime_candidate)


    choice=input("Would you like to run the program again (y/n) ").lower()
    if choice!='y':
        running=False
