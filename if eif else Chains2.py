print("What if/elif/else ")


age=int(input("What is your age : "))

if age<18:
    print("You are only ",age," ! ")
    print("You can not gamble !! ")
elif age<21:
    print("You are only ",age," ! ")
    print("You can play Blackjack but you can not have drink !!! ")
elif age<100:
    print("Okay good. You are ",age," !! ")
    print("You can play Blackjack and you can drink !! ")
else:
    print("What are you doing out at a casino !?!?!? ")

print("-------------------------------------------------------")

num=int(input("Please enter number "))
if num<5:
     print("That is small number ")
elif num<10:
    print("That is sort of small ")
elif num<15:
    print("That is a medium number ")
elif num<20:
    print("That is sort of medium ")
elif num<=25:
    print("That is a large number ")
elif num==40:
    print("I love that number ")
else :
    print("That number is  HUGE ! ")

