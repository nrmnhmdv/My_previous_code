print("Welcome to the Guess My Word App ")


game_dict={
    "sports":['basketball','baseball','soccer','football','tennis','curling'],
    "colors":['orange','yellow','purple','aqumarine','violet','gold'],
    "fruits":['apple','banana','watermelon','peach','mango','steawberry'],
    "classes":['english','history','science','mathematics','art','health'],
    }

game_keys=[]

for key in game_dict.keys():
    game_keys.append(key)

running=True
while running:
    pass

data={0,1,2}
for i in data:
    print(data.add(i))

    choice=input("Would you like to run agin the program (y/n)").lower()
    if choice!='y':
        running=False
        print("Thank for using Guess My Word App ")
