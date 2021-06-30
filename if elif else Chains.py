print(" if/elif/else Chains ")

age=int(input("What is your age : "))

if age<18:
    print("You are only ",age,"!")
    print("You can not gamble ")
elif age<21:
    print("Okay, so you are ",age,"!!")
    print("You can play Blackjack but you can not have a drink.")
elif age<100 :
    print("Okay good .You are",age,"!")
    print("You can play Blackjack and you can have drink ...")
else:
    print("What are you doing out casino !?!?")

