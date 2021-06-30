print("Yes or no polling App")

#Get user input
issue=input("What is the yes or no issue you will be voting on today : ")
vote_number=int(input("What is the number of voters you will allow on the issue : "))
password=input("Enter a password for the polling results : ")

#Initilize iur variables

yes=0
no=0
results={}

#Simulate voting

for i in range(vote_number):
    name=input("\nEnter your full name : ").title().strip()
    if name in results.keys():
        print("Sorry, it seems that someone with that name has already voted ")
    else:
        print("Here is our issue : ",issue)
        choice=input("What do you think.... yes or no : ").lower().strip()
        if choice=='yes' or choice=='y':
            choice='yes'
            yes+=1
        elif choice=='no' or  choice=='n':
            choice='no'
            no+=1
        else:
            print("That is not a yes or no answer, but okay...")
        # Add vote to the dictionary results
        results[name]=choice
        print("Thank you ",name,"! Your vote has been recorded ")

# Show who actually voted
total_votes=len(results.keys())
print("\nThe following ",total_votes," people voted :")
for key in results.keys():
    print(key)

# Summarize the voting results
print("\n On the following issue : ",issue)

if yes>no:
    print("Yes wins !",yes," votes to ",no,".")
elif no>yes:
    print("No wins !",no," votes to ",yes," . ")
else:
    print("It was a tie ",no," votes to ",yes)

#Allow the admin to see the actual votes 
guess=input("\n To see the voying results enter the admin password ")
if guess==password:
    for key,value in results.items():
        print("Username ",key.title(),"\t\tVotes ",value)
else:
    print("Sorry , that is not the correct password.Goodbay ")


print("\n Thank you for using the Yes or No Issue Polling App")




























