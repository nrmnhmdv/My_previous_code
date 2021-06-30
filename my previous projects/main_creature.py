from creature import Creature

def show_menu(creature):

    if creature.is_sleeping:
        choice = input(" \n Enter (6) to try and wake up : ")
        choice = '6'
    else:
        print("\n Enter (1) to eat .")
        print("\n Enter (2) to play .")
        print("\n Enter (3) to sleep .")
        print("\n Enter (4) take a bath .")
        print("\n Enter (5) tp forage for food .")
        choice = input(" What is your choice : ")
    return choice

def call_action(creature, choice):

    if choice == '1':
        creature.eat()
    elif choice == '2':
        creature.play()
    elif choice == '3':
        creature.sleep()
    elif choice == '4':
        creature.clean()
    elif choice == '5':
        creature.forage()
    elif choice == '6':
        creature.awake()
    else:
        print(" User entered a non valid choice ")
print(" Welcome to the Pytonagachi Simulator App ")

difficulty = int(input(" Please choose a difficulty (1-5) : "))

if difficulty >= 5:
    difficulty = 5

elif difficulty <= 1:
    difficulty = 1

running = True
while running:
    name = input(" Please enter creature's name : ")
    player = Creature(name)
    raund = 1
    while player.is_alive:

        print(" Round : ", raund)
        player.show_values()
        round_move = show_menu(player)
        call_action(player, round_move)
        print(" \n Raund", raund, " Summary :")
        player.show_values()

        input(" Click Enter ")
        player.incriment_values(difficulty)
        player.kill()
        raund += 1

    print("\nR.I.P.")
    print(player.name + " survived a total of " + str(raund-1) + " rounds.")

 #Ask the user to play again.
    choice = input("Would you like to play again (y/n): ").lower()
    if choice != 'y':
        running = False
        print("Thank you for playing Pythonagachi!")
