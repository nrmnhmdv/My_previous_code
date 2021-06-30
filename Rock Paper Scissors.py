import random
print("Welcome to a game of Rock ,Paper,Scissors")
rounds=int(input("How many rounds would you like to play :"))

moves=['rock','paper','scissors']

p_score=0
c_score=0


for game_raound in range(0,rounds):
    print("\n Round",game_raound+1)
    print("Player ",p_score,"\t Computer",c_score)

    c_index=random.randint(0,2)
    c_choice=moves[c_index]
    #get the players move
    p_choice=input("Time to pick rock,paper scissors :").lower().strip()
    #if the player makes a valid move

    if p_choice in moves:
        print("\tComputer",c_choice)
        print("\tPlayer",p_choice)
        # Computer chooses rock
        if p_choice=='rock'and c_choice=='rock':
            winner='tie'
            phrase="It is a tie , how boring"
        elif p_choice=='paper'and c_choice=='rock':
            winner='player'
            phrase='Paper covers rock!'
        elif p_choice=='scissors'and c_choice=='rock':
            winner='computer'
            phrase='Rock smashes scissors!'
        #computer chooses paper
        elif p_choice=='rock'and c_choice=='paper':
            winner='Computer'
            phrase="Paper covers rock"
        elif p_choice=='paper'and c_choice=='paper':
            winner='tie'
            phrase='It is a tie how boring!'
        elif p_choice=='scissors'and c_choice=='paper':
            winner='player'
            phrase='Scissors cut paper !'
        #Computer  chooses scissors
        elif p_choice=='rock'and c_choice=='scissors':
            winner='player'
            phrase="Rock smashes scissors"
        elif p_choice=='paper'and c_choice=='scissors':
            winner='computer'
            phrase='Scissors cut paper !'
        elif p_choice=='scissors'and c_choice=='scissors':
            winner='Tie'
            phrase='It is a tie how boring !'
        else:
            print("Round winner not calculated.")
            winner='tie'
            phrase='It is a tie , how boring'
        # Display round results
        print("\t"+phrase)
        if  winner=='player':
             print("\tYou win round ",(game_raound+1)," .")
             p_score += 1
        elif winner=='computer':
            print("\t Computer wins round ",(game_raound+1)," . ")
            c_score+=1
        else:
            print("\t This round was a tie")

    else:
        print("That is not a valid game option !")
        print("Computer gets the point!")
        c_score+=1

print("\n Final Game Results ")
print("\t Rounds Played ",rounds)
print("\t Player score: ",p_score)
print("\tComputer Score :",c_score)

if p_score>c_score:
    print("\t Winner Player ")
elif c_score>p_score:
    print("\t Winner Computer ")
else:
    print("\t The game was a tie")



