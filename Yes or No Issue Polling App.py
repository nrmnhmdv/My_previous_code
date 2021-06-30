print("Welcome to the Yes or No Issue Polling App My own algorithm ")

issue=input("What is the yes or no issue you will be voting on today :")

votes_range=int(input("What is the number of voters you will allow on the issue :"))


vote_dictionary={}

recorded=0
not_recorded=0
for i in range(votes_range):
    
    password=input('\n'"Enter a password for polling results :")
    full_name=input('\t'"Enter your full name :")
    
    vote_dictionary[full_name]=password
    
    
    print('\t'"Here is our issue : ",issue)
    choice=input('\t'"What do you think... yes or no ").strip()
    if choice=='y':
        print('\t'"Thank you ",full_name.title(),"!","Your vote has been recorded")
        recorded+=1
    else:
        print('\t'"Thank you ",full_name.title(),"!","Your vote of no has been recorded")
        not_recorded+=1

        
print("The following ",votes_range,"people voted :")
for keys in vote_dictionary.keys():
    print(keys.title())
print('\n')
print("On the following issue :",issue)

if recorded>not_recorded:
    print("Yes wins !!",recorded,"votes to ",not_recorded)
elif recorded==not_recorded:
    print("Equal")
else:
    print("Lose ",recorded,"votes to",not_recorded)
    
