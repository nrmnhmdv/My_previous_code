print(" Welcome to the Voter Registration App ")

name=input("Please enter your name ")
age=int(input("Please enter your age "))

parties=["Republican","Democratic","Independent","Libertarian","Green"]
if age<18:
    print("You are not old enough to register to vote ")
else:
    print("Congratulations ",name.title(),"You are old enough to register to vote ")
    
    for parti in parties:
        print('\t'"-",parti)

    choice=input("What party would you like to join :").title().strip()

    if choice.title()==parties[0]:
        print("That is major party !!! ")
        print("Congratulations ",name,"You have joined  the party")
    else:
        print("That is not major party")
        print("Congratulations ",name," you have joined  the party")
