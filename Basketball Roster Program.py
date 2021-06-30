print("Wellcome to the Basketball Roster Program")
players=[]
players.append(input("Who is your point guard :"))
players.append(input("Who is your shooting guard :"))
players.append(input("Who is your small guard : "))
players.append(input("Who is your power guard : "))
players.append(input("Who is your center :"))
#print(players)

print('\t\t'"Your starting",len(players),"for the upcoming basketball season")
print('\t\t\t'"Point Guard : ",players[0].title())
print('\t\t\t'"Shooting Guard :",players[1].title())
print('\t\t\t'"Small Forward : ",players[2].title())
print('\t\t\t'"Power Forward : ",players[3].title())
print('\t\t\t\t'"  Center :  ",players[4].title())

injured_player=players.pop(2)

print("Oh no ",injured_player,"is injured ")
print("Your roster only has ", len(players)," players ")

new_player=input("Who will take"+injured_player.title()+" spot :").title()
players.insert(2,new_player)
#print(players[2])
print('\t\t'"Your starting",len(players),"for the upcoming basketball season")
print('\t\t\t'"Point Guard : ",players[0].title())
print('\t\t\t'"Shooting Guard :",players[1].title())
print('\t\t\t'"Small Forward : ",players[2].title())
print('\t\t\t'"Power Forward : ",players[3].title())
print('\t\t\t'"     Center  : ",players[4].title())

print("Good luck",new_player,"you will do grat ")
print("Your roster now has ",len(players)," players ")

