print("Through Multiple List ")

names=["jack","john","mark","bill"]
numbers=[20,3,14,44]

for i in range(len(names)):
    print(names[i].title()+":"+str(numbers[i]))

print()
print("Useng with ZIP FUNCTION ")
print()
for name, number in zip(names,numbers):
    print(name.title()+":"+str(number))
