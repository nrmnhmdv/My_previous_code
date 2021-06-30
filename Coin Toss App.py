import random

print("Welcome to the Coin Toss App")

print("I will flip a coin a set number of times")

#Get user input 
flip_number=int(input("How many times would you like me to flip the coin :"))
choice=input("Would you like to see the result of each flip (y/n)").lower()

print("\n Flipping !!!!\n ")

#Initialize variables

head=0
tails=0


#The main loop

for flip in range(flip_number):
    #Create the coin object
    coin=random.randint(0,1)

    if coin==1:
        head+=1
        if choice.startswith('y'):
            print("HEADS")
    else:
        tails+=1
        if choice.startswith('y'):
            print("TAILS")
    if head== tails:
        print("At " + str(flip + 1) + " flips, the number of heads and tails were equal at " + str(head) + " each.")

#Calculate percentages

head_percentage=round(100*head/flip_number,2)
tails_percentage=round(100*tails/flip_number,2)


print("\nResults of Flipping a Coin " + str(flip_number) + " Times: ")
print("\nSide\t\tCount\t\tPercentage")
print("Heads\t\t" + str(head) + "/" + str(flip_number) + "\t\t" +str(head_percentage) + "%")
print("Tails\t\t" + str(tails) + "/" + str(flip_number) + "\t\t" +str(tails_percentage) + "%")






















