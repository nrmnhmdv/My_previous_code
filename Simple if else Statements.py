print("Simple if/else Statements ")
print()

colors=['green','red','blue','pruple']

for color in colors:
    print(color,end=' ')
print()

for color in colors:
    if color=='red':
        print(color.upper())
        print("I love the color",color.upper())
    else:
        print(color)
        print("The color ",color,"is okay")


print("----------------------------------")
age=int(input(" Please enter your age "))

if age>=21:
    print("Have drink")
else :
    print("Ah , no drinks for you ! ")

print("----------------------------------")
first_name="David"
last_name="Smith"

if first_name=="David" and last_name=="Smith":
    print("You are so cool guy")

else:
    print("Not enough cool")

print("-------------------------------------")
if first_name=="David" or last_name=="Jones":
    print("You are a great guy ! ")

else:
    print("Not great enough ....")






















