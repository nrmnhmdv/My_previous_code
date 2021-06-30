import random
print("Welcome to the My Guess Word App")

game_dict={
       "sports":['basketball','baseball','soccer','football','tennis ','curling'],
       "colors":['orange','yellow','purple','aquamarine','violet','gold'],
       "fruits":['apple','banana','watermelon','peach','mango','strawberry'],
       "classes":['english','history','science','mathematics','art','health'],
    }

game_keys=[]

for key in game_dict.keys():
    game_keys.append(key)

#The main game loop

playing=True

while playing:
    game_category=game_keys[random.randint(0,len(game_keys)-1)]
    #print(game_catogory)
    #input()
    # Randomly pick the game category and the game word from the game dictionary
    game_word=game_dict[game_category][random.randint(0,len(game_dict[game_category])-1)]

    #bild a dashed "-" word to represent the game word
    blank_word=[]
    for letter in game_word:
         blank_word.append("-")
    print("Guess a", len(game_word)," letter wrod from the following")

    guess=""
    guess_count=0

    # a single round loop
    while guess != game_word:
        print("".join(blank_word))
        guess=input("\n Enter your guess ").lower()
        guess_count += 1

        # Guess is correct user won the game

        if guess ==  game_word:
            print("\n Correct ! Yon guessed the word  in ",guess_count," guesses .")
            break
        # Guess is incorrect user must keep guessing
        else:
            print("That is not correct . let us revael a letter to help you ! ")
            # Loop to replace  in "-" blank_word
            swapping=True
            while swapping:
                letter_index=random.randint(0,len(game_word)-1)

                if blank_word[letter_index] == "-":
                    blank_word[letter_index]=game_word[letter_index]
                    swapping=False

    choice=input("Would you like to play again ? (y/n)").lower()
    if choice!='y':
        playing=False
        print("Thank you for Playing The Game ")
            


















































    
