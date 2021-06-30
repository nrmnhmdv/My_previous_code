print("Welcome to the Fibonacci Calculator App ")

num=int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

fib=[1,1]

for i in range(num-2):
    new_fib=fib[i]+fib[i+1]
    fib.append(new_fib)
    
#display the fib values 
print("\n The first "+str(num)+"numbers of the Fibonaci Sequence are ")

for number in fib:
    print(number)

#Compute the golden ratio

golden=[]

for i in range (len(fib)-1):
    ratio=fib[i+1]/fib[i]
    golden.append(ratio)
print("\nThe corresponding Golden Ratio values are: ")
for ratio in golden:
    print(ratio)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")
