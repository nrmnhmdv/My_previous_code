print("Pythonagachi Simulator App")
import random
import os
# Define the creature class
class Creature():
    """ Create a simple Tomogachi clone """

    def __init__(self,name):
        """Initialize attributes"""
        self.name=name.title()
        # Attributes to track playing the game (0-10)
        self.hunger=0
        self.bordem=0
        self.tiredness=0
        self.dirtiness=0

        self.food=2  #represet food inventory
        self.is_sleeping=False  #Bool to track if creature is sleeping
        self.is_alive=True  #Bool to track creature is alive

    def eat(self):
        """Simulate eating"""
        if self.food>0:
            self.hunger-=1
            self.hunger-=random.randint(1,4)
            print("Yumm !! "+self.name," ate a great meal ")
        else:
            print(self.name," does'nt have any food ")
        # if the hunger is less  than zero, set it to zero
        if self.hunger<0:
            self.hunger=0

    def play(self):
        """Play a gussening game to lower"""
        value=random.randint(0,2)
        print("\n",self.name," Wants to play a game")
        print(self.name+"is thinking of a number 0, 1 or 2")
        guess=int(input("What is your guess : "))
        # lower the boredom attribute based on the users guess
        if guess==value:
            print("That is correct!!! ")
            self.bordem-=3
        else:
            print("WRONG !!",self.name+" was thinking of ",str(value),".")
            self.bordem-=1
        # if the bordem is less then  zero
        if self.bordem<0:
            self.bordem=0

    def sleep(self):
        """Simulate sleping The only """
        #Put the creature to sleep
        self.is_sleeping=True
        self.tiredness-=3
        self.bordem-=2
        print("Zzzzzz........Zzzzzz........Zzzzzz........")
        # If tiredness or bordem is less than zero
        if self.tiredness <0 :
            self.tiredness=0
        if self.bordem<0:
            self.bordem=0

    def awake(self):
        # Creature has a 1/3 chance to randomly wake up
        value=random.randint(0,2)
        if value==0:
            print(self.name+" Just woke Up !")
            self.is_sleeping=False
            self.tiredness=0
        else:
            print(self.name+ " won't wake up")
            self.sleep()

    def clean(self):
        """ Simulate taking a bath to completely clean the creature"""
        self.dirtiness=0
        print(self.name+ " has taken a bath . All clean ! ")


    def forage(self):
        """ Simulate foraging for food """
        # Randomly find food 0 to 4 peices
        food_found=random.randint(0,4)
        self.food+=food_found
        # Creature gets dirty from foraging
        self.dirtiness+=2
        print(self.name+" found "+str(food_found)+" pices of food ")



    def show_values(self):
        """Show teh current inforation about the creatures"""
        print("\n Creature Name :"+self.name)
        print(" Hunger (0-10)",self.hunger)
        print("Boredom (0-10)",self.bordem)
        print("Tiredness (0-10)",self.tiredness)
        print(" Dirtiness (0-10)",self.dirtiness)

        print("\n Food Inventory ",str(self.food))

        #Show current sleeping status
        if self.is_sleeping:
            print("Current Status : Sleeping ")
        else:
            print("Current Status : Awake ")

    def incriment_values(self,diff):
        """ User must set an arbitrary difficulty."""
        """ Update the current values """
        self.hunger+=random.randint(0,diff)
        self.dirtiness+=random.randint(0,diff)
        if self.is_sleeping == False:
            self.bordem += random.randint(0,diff)
            self.tiredness

    def kill(self):
        """ Check  for all conditions to kill or sleep"""
        #put the creture kill
        if self.hunger >= 10:
            print(self.name+" has starved to death...")
            self.is_alive=False

        elif self.dirtiness>=10:
            print(self.name+" has suffered an infection and died ")
            self.is_alive=False
    # put the creature sleep
        elif self.bordem>=10:
            self.bordem=10
            print(self.name+" is bored . Falling asleep....")
            self.is_sleeping=True
        elif self.tiredness>=10:
            self.tiredness=10
            print(self.name+" is sleepy. Falling asleep..")
            self.is_sleeping=True


# Helper functions
def show_menu(creature):
    """ Show the menu for the player """
    if creature.is_sleeping:
        choice=input("\n Enter (6 ) to try and wake up ... ")
        choice='6'
    else:
        print("\n Enter (1) to eat ")
        print("Enter (2) to play ")
        print("Enter (3) to sleep ")
        print(" Enter (4) to take a bath ")
        print("Enter (5) to forage for food .")
        choice=input("What is your choice : ")
    return choice


def call_action(creature,choice):
    # Call the apporpritate creature class
    if choice=='1':
        creature.eat()
    elif choice=='2':
        creature.play()
    elif choice=='3':
        creature.sleep()
    elif choice=='4':
        creature.clean()
    elif choice=='5':
        creature.forage()
    elif choice=='6':
        creature.awake()
    else:
        print(" Sorry, that is not valid move ")

# The main code
print("Welcome to the Pythonagachi Simulator App ")

# Set the difficulty level
difficulty=int(input("Please choose a difficulty level (1-5) : "))
if difficulty>5:
    difficulty=5
elif difficulty<1:
    difficulty=1

running=True

while running:
    name=input("What name would you like to give your  pet Pythonagachi ? ")
    player=Creature(name)

    rounds=1
    # The game loop that simulate an individual round
    #This loop should run as long as the creature is alive

    while player.is_alive:
        print("/n-------------------------------------------")
        print(" Round # "+str(rounds))
        # Individual round should show values ,get a players move
        player.show_values()
        round_move = show_menu(player)
        call_action(player, round_move)

        print("Round # "+str(rounds)+" Summary ")

        player.show_values()
        input("\n Press (enter) to continue .... ")

        #Increment values and check for death
        player.incriment_values(difficulty)
        player.kill()
        # Round is over
        rounds += 1

    #the creature has died ,Game is over
    print("\nR.I.P")
    print(player.name + " survived a total of  "+str(rounds-1))

    #Ask the user to play agin
    choice = input(" Wold you like to play again (y/n) ?").lower()
    if choice != 'y':
        running = False
        print(" Thank you for playing Pythonagachi App ")


