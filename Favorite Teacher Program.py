print("Welcome to the Favorite Teacher Program")
teachers=[]


teachers.append(input("Who is your first favorite teacher :").title())
teachers.append(input("Who is your second favorite teacher :").title())

teachers.append(input("Who is your thrid favorite teacher :").title())
teachers.append(input("Who is your forth favorite teacher :").title())

print("Your favorite teachers rank are ",teachers)
print("Your favorite teachers rank are ",str(sorted(teachers)))
print("Your favorite teachers rank are ",str(sorted(teachers,reverse=True)))
print("You have a total of",len(teachers),"favorite teachers ")

new_teacher=input("Oops "+teachers[0]+"is no your first favorite teacher. Who is your new FAVORITE teacher :").title()

teachers.insert(0,new_teacher)
print("Your favorite teachers rank are ",teachers)
print("Your favorite teachers rank are ",str(sorted(teachers)))
print("Your favorite teachers rank are ",str(sorted(teachers,reverse=True)))
print("You have a total of",len(teachers),"favorite teachers ")

print("Your top two teachers are :",teachers[0]," and ",teachers[1])
print("Your next two favorite teachers are :",teachers[2]," and ",teachers[3])
print("Your last favorite teacher is : ",teachers[4])
print("You have total",len(teachers)," favorite teachers ")

removed_teacher=input("You've decided you no longer like a teacher. Which teacher would you like to remove from you of lits ")
teachers.remove(removed_teacher.title())
print("Your favorite teachers rank are ",teachers)
print("Your favorite teachers rank are ",str(sorted(teachers)))
print("Your favorite teachers rank are ",str(sorted(teachers,reverse=True)))
print("You have a total of",len(teachers),"favorite teachers ")

print()

print("Your top two teachers are :",teachers[0]," and ",teachers[1])
print("Your next two favorite teachers are :",teachers[2]," and ",teachers[3])
print("Your last favorite teacher is : ",teachers[3])
print("You have total",len(teachers)," favorite teachers ")
