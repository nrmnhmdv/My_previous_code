topics=["Algebra","Computer Science","Art","Math"]
print(topics)

topics_2=["Computer Science","Art","Math","Algebra"]

print(topics[0])
print(topics_2[0])
print(topics[3])
print(topics_2[3])
print(type(topics[3]))
print(type(topics))

print("My favorite area of study is " + topics[1].upper())

color=["green","orange","red","purple","yellow","blue","black","pink","white"]
print(color[4])
print(color[-1])

color.append("silver")
color.append("gold")
print(color)
color.insert(2,"brown")
print(color)
color.remove("yellow")
print(color)
# sondan silir

removed_color=color.pop()
print("Removing  the element of color is  " + removed_color)

bad_color=color.pop(7)
print("A bad color is " + bad_color)
# including list dynamiclly
fruit=[]
fruit.append(input("What is your favorite fruit ? "))
fruit.append(input("What is your favorite fruit ? "))
fruit.append(input("What is your favorite fruit ? "))
fruit.append(input("What is your favorite fruit ? "))
print(fruit)

# for the sorting list
sports=["swimming","regby","futball","succer","baseball","golf"]
print("The original list of  : ",sports)
print(sorted(sports))
#  sorted olunmus listi tersine cevirir
print(sorted(sports,reverse=True))

grades=[88,74,67,29,100,57,89,53,90,98]
print(grades)
print(sorted(grades))
print(sorted(grades,reverse=True))
# listlerin sorted olunmasi sadece temproray di
print(grades)
grades_length=len(grades)
print(grades_length)
print(type(grades_length))
# removing something
removed_grades=grades.pop()
print("Removed element of grades " +str(removed_grades))
# when we used .sort() function we can changed permanently
grades.sort()
print("Permanently changing  of list ")
print(grades)
# reverse permenantly 
grades.sort(reverse=True)
print("Reverse permenantly " ,grades)

sports.reverse()
print("Reverse of lists ",sports)





























