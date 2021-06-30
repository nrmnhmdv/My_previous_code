print(" Wellcome to the Grade Sorter Application ")
grades=[]
first_grade=grades.append(int(input("What is your first grade (0-100) ")))

second_grade= grades.append(int(input("What is your second grade (0-100) ")))
thrid_grade= grades.append(int(input("What is your thrid grade (0-100) ")))
fourth_grade= grades.append(int(input("What is your fourth grade (0-100) ")))

print( "Your grades are : ",grades)

print("Your grades from highest to lower are :",grades.sort(reverse=True))
grades.sort(reverse=True)

print("The lowest two grades will now be dropped ")
removed_element1=grades.pop()
removed_element2=grades.pop()

print("Removed grade element  ",removed_element1)
print("Removed grades element " , removed_element2)

print("Your remaning grades are :", str(grades))
print("Your highest grades is ",str(grades[0]))

 

