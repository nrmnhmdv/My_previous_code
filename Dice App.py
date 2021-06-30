import random

def dice_sides():
    """Ask the user how many sides on their die"""
    sides=int(input("How many sides would you like on your dice :"))
    return sides 

def dice_number():
    """ Ask the user how many dice to roll """
    number=int(input("How many dices would you like to roll :"))
    return number

 
def roll_dice(sides,number):
    """Simulate rolling the  dice """
    dice=[]
    print("\n You rolled ",number," ", sides," sided dice .")
    print("\n-----Results are as followed-----")
    for i in range(number):
        value=random.randint(1,sides)
        print("\t",value)
        dice.append(value)
    return dice


def sum_dice(dice):
    """ Add all values of dice in a list """
    total=0
    for die in dice:
        total+=die
    print("The total value of your roll is ",total," . ")
    


def roll_again():
    """ Ask the user to roll again """
    choice=input("\n Would you like to roll again (y/n) : ")
    if choice !='y':
        roll=False
    else:
        roll=True
    return roll

# The main code

print("Welcome to the Python Dice App ")

rolling=True

while rolling:
    #Get the info for the type dice
    d_side=dice_sides()
    d_number=dice_number()

    # Roll  and sum the dice
    my_dice=roll_dice(d_side,d_number)
    sum_dice(my_dice)

    # roll again
    rolling=roll_again()
print("Thank you for using the Python Dice App ")


new_list=['a',1,'b',3]
print(new_list)
new_list='danger'
print(len(new_list))
new_list="danger"
print(len(new_list))


rainbow="red,orange,yellow,green,blue,indigo,violet"
warm_colors="red,yellow,orange"
my_colors="orange"

if my_colors in rainbow:
    print("Wow , your color is in the rainbow!")
    if my_colors in warm_colors:
        print("Oh,by the way, it's a warm color.")
print(rainbow[2])


























































    
