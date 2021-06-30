import datetime
print("Wellcome to the Grocery List App ")

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)


foods=["Meat ","Cheese"]
print("Current  Date and Time :",month,'/',day,' ',hour,':',minute)
print("You currently Have",foods[0]," and ",foods[1],"in your list")

food=foods.append(input("Type of food add to the grocery list "))
food=foods.append(input("Type of food add to the grocery list "))
food=foods.append(input("Type of food add to the grocery list "))

print(foods)

print("\t\t  Simulating grocery shopping....")
print("Current grocery list",str(len(foods)),"items")
print(foods)

buy_food=(input("What food did you just buy ? "))
foods.remove(buy_food)
print("Removing",buy_food,"from list")
print("Current grocery list ",len(foods),"items")
print(foods)

buy_food=(input("What food did you just buy ? "))
foods.remove(buy_food)
print("Removing",buy_food,"from list")
print("Current grocery list ",len(foods),"items")
print(foods)

buy_food=(input("What food did you just buy ? "))
foods.remove(buy_food)
print("Removing",buy_food,"from list")
print("Current grocery list ",len(foods),"items")
print(foods)


no_item = foods.pop()
print("\nSorry, the store is out of " + no_item + ".")
new_food = input("What food would you like instead: ").title()
foods.insert(0, new_food)

print("\nHere is what remains on your grocery list: ")
print(foods)











