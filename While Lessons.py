print("WElcome to the While Lesson ")
#While loops
# for loops running a set of times
# while loops running until a certain is met

for i in range(11):
    print(i)

#initilazie i

print("-------------------------------")
i=0
while i<=10:
    print(i)
    i+=1
current_num=1
print("---------------------------")

while True:
    print(current_num)
    current_num+=1
    choice=input("Press enter to print the next number or q to quit :").lower()
    if choice=='q':
        break

current_num1=0
while current_num1<10:
    current_num1+=1
    if current_num1%2==0:
        print(current_num1,"is Even !")
    else:
        print(current_num1,"is Odd ! ")



current_number2=1
playing=True

while playing:
    if current_number2%3==0:
        print(current_number2," is divisible by 3 ! ")
    
    else:
        print("Not divisible by 3")

    choice=input("Enter 'n' to stop or press enter to continue ")
    if choice=='n':
        playing=False

    current_number2+=1


print(current_number2)
print("Quitting....")

num=10
while num>0:
    num-=1
    if num%4==0:
        continue
    #num-=1
    print("Current variable  ",num)

print("All done")
























































