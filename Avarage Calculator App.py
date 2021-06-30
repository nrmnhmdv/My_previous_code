print("Welcome to the Average Calculator App ")

name=input("What is your name ? ")

number=int(input("How many grades would you like to enter "))

list_num=[]

for i in range(number):
    element=int(input("Enter grade : "))
    list_num.append(element)

print(list_num)

print(" Grades Highet to Lowest ")

list_num.sort(reverse=True)

print(list_num)

avarage=0
summ=0
for i in list_num:
    summ=summ+i
    avarage=summ/number

print(name.title()," Grade Summary : ")
print("\t\t Total Number of Grades :",number)
print("\t\t Highest Grade :",max(list_num))
print("\t\t Lowest Grade :",min(list_num))
print("\t\t Average :",avarage)

desired_avg=int(input("what is your desired average : "))
grade_req = desired_avg*(len(list_num)+1) - sum(list_num)
grade_req = round(grade_req, 2)
print("Good luck ",name.title())
print("You will need to get a " + str(grade_req) + " on your next assignment to earn a " + str(desired_avg) + " average.")

new_list=list_num[:]
print("\n Lets see what you avarege could have been if you did better/worse on an assignment")

grade_change=int(input("What grade would you like to change: "))
new_list.remove(grade_change)

new_grade=int(input("What grade would you like to change "+str(grade_change)+" to "))

new_list.append(new_grade)

print("New list ",new_list)
new_avarage=0
summ=0
for i in new_list:
    summ=summ+i
    new_avarage=summ/number

print(name.title()," Grade Summary : ")
print("\t\t Total Number of Grades :",number)
print("\t\t Highest Grade :",max(new_list))
print("\t\t Lowest Grade :",min(new_list))
print("\t\t Average :",new_avarage)

print("Your new average would be a ",desired_avg ," compared to your real average of ",avarage )

c=desired_avg-avarage
print("That is a change of ",c," points! ")

print("\nToo bad your original grades are still the same!")
print(list_num)
print("You should go ask for extra credit!")




















