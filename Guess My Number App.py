import random
print("Welcome to the Guess My Number App")
name=input("Hello ! What is your name :").title().strip()
print("Well ",name,"I am thinking of a number between 1 and 20 ")



my_guess=random.randint(1,20)

for i in  range(0,5):
    your_guess=int(input("Take a gues : "))   
    if your_guess<my_guess:
        print("Your guess is too low ")
    elif your_guess>my_guess:
        print("Your guess is too high ")
    else:
        break

if your_guess==my_guess:
    print("Good job ",name )
        #break
else:
    print("Game Over.The number I was thinking of was ",my_guess," . ")
