print("Welcome to the Factor Generator App MY OWN ALGORITHM ")

print("WITH FOR LOOP ")
n=int(input("Please enter a number "))
list1=[]

for i in range(1,n+1):
    c=n%i
    if c==0:
        print(i)
        list1.append(i)

print()
for i in range(int(len(list1)/2)):
    print(list1[i],"*",list1[-i-1],"=",n)

print("----------------------")
print("WITH WHILE LOOP ")

m=int(input("Please enter a number "))

j=1
list2=[]

while j<m+1:
    #i=1
    c=m%j
    if c==0:
        print(j)
        list2.append(j)
    j+=1
print()

for j in range(int(len(list2)/2)):
    print(list2[j],"*",list2[-j-1],"=",m)  
