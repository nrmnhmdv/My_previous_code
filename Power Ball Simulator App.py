import random
print("Welcome to the Power Ball Simulator")

print("------------------Power Ball Simulator-----------------")

# determine the size of the lottery
white_balls=int(input("How many white balls to draw from for 5 winning numbers (Normally 69) : "))
if white_balls<5:
    white_balls=5
#Get the number of red balls

red_balls=int(input("How many red-balls to draw from for the Power Ball (Normally 26) : "))
if red_balls<1:
    red_balls=1

#Calculate the odds of winning this specific lottery

odd=1
for i in range(5):
    #example multiplation for generating odd to win
    #(69*68*67*66*65)*26/120
    odd *=white_balls-i
odd*=red_balls/120
print("You have a 1 in",odd," chance of winning this lottery. ")

#Get ticket interval
ticket_interval=int(input("Putchase tickets in what interval : "))

#Generate the winning lottery number
winning_numbers=[]
while len(winning_numbers)<5:
    number=random.randint(1,white_balls)
    if number not in winning_numbers:
        winning_numbers.append(number)
winning_numbers.sort()

#Get the red ball for the ticket

number=random.randint(1,red_balls)
winning_numbers.append(number)

# Simulate the powerball drawing
print("\n----------------Welcome to the Power Ball-----------------------")
print("\nTonight is winning numbers are :" ,end=" ")

for number in winning_numbers:
    print(number,end=' ')
input("\n Press 'Enter' to begin purchasing tickets !!!! ")

#Purchase tickets in the set interval
tickets_purchased=0
active=True
tickets_sold=[]
#Run the lottery if we have not purchased the winning the ticket and we still want to play

while winning_numbers not in tickets_sold and active==True:
    # make a new lottery tickets for the user to buy
    lottery_numbers=[]
    while len(lottery_numbers)<5:
        if number not in lottery_numbers:
            lottery_numbers.append(number)
    lottery_numbers.sort()

    number=random.randint(1,red_balls)
    lottery_numbers.append(red_balls)

    #This current ticket has not yet been sold

    if lottery_numbers not in tickets_sold:
        tickets_sold+=1
        tickets_sold.append(lottery_numbers)
    print(lottery_numbers)












    














































    


























