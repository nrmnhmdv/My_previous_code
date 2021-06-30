print("While Lessons ")

numbers=list(range(1,11))
print(numbers)

while numbers:
    numbers.pop()
    print(numbers)
print("------------------------------------")
numbers1=[4,14,4,3,9,0,4,2,4]
while 4 in numbers1:
    numbers1.remove(4)
    print(numbers1)
print("All 4 is removed ")


flag1=True
flag2=True

while flag1:
    print("While loop 1 is running")
    while flag2:
        print("While loop 2 is runing ")
        choice=input("Continue rununing while loop 2 (y/n) ")
        if choice.lower()!='y':
            flag2=False
            print("Ending while loop 2 ")
            break
    choice=input("Continue running while loop1 (y/n) ")
    if choice.lower()!='y':
        flag1=True
        print("Ending while loop 1 ")
        break
