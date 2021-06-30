import random
print("Welcome to the Thesaurus App !")
print("Choose a word from the thesaurus and I will give you a synonym")
synonyms={
    'hot':['balmy','summery','tropical','boiling','scorching'],
    'cold':['chilly','cool','freezing','frigid','polar'],
    'happy':['content','cheery','merry','jovial','jocular'],
    'sad':['unhappy','downcast','miserable','glum','melancholy'],
    }

print("Here are the words in the thesaurus :")
for key in synonyms.keys():
    print('\t'"-",key)

choose=input("What word would you like a synonym for ")

if choose in synonyms.keys():
    index=random.randint(0,4)
    print("A synonym for",choose," is ",synonyms[choose][index])
else:
    print(" I am sorry, that word is not currently in the synonyms.")

choose_2=input("Would you like to see the whole synonyms ?(yes/no)").lower().strip()

if choose_2=='yes':
    for key, values in synonyms.items():
        print('\n',key.title())
        for value in values:
            print('\t',value)
else:
    print("I hope you enjoed the program.Thank you !!!")
