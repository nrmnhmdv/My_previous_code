print("Welcome to the Fibonacci Calculator  App")
print("\t\t\t""MY OWN ALGORITHM ")

number=int(input("How many digits of the Fibonacci  Sequence would you like to compute? "))

begin=1
itarete=1

print("The first ",number,"numbers of the Fibonacci sequence are :")
print(begin)
print(itarete)

 
for i in range(1,number+1):
    temp=itarete+begin
    begin=itarete
    itarete=temp
    print(itarete)


print("The Golden Ratio ")

begin=1
itarete=1
for i in range(1,number+1):
    rastio=itarete/begin
    temp=itarete+begin
    begin=itarete
    itarete=temp
    #max_value=max(rastio)
    print(rastio)


print("The ratio of consecutive Fibonacci terms approaches Phi: 1.618...")
