print("Welcome Control Statemenst break continue and pass")

print("Break statements ")
for i in range(1,11):
    if i==5:
        break
    print(i)
print("-----------------------")

print("Continue statements ")
for i in range(1,11):
    if i==4:
        continue
    print(i)


print("----------------------------")
print("Pass statements ")
for i in range(1,11):
    if i==3:
        pass
    print(i)

# break - stops the whole loop
#continue stops current iteration of the loop
# pass - passes over the current statement and continues the loop as a normal

print("--------------------------------")

for i in range(1,11):
    if i==8:
        break
    elif i==5:
        continue
    elif i==6:
        pass
    print(i)
