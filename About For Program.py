print("Welcome about to the For Program ")
print("More about Lists  using for with Lists")

teams=["giants","bills","jets","patriots"]

print(teams)
n=teams[0].title()
#print(n)
for team in teams:
    print(team.title())
    print("You are going to win the Super Bowl!\n")

print("Go Football!!!")


values=[1,2,3,4,5]

total_sum=0
for value in values:
    total_sum += value
print("Total sum is",total_sum)



triples=[["a","b","c"],["1","2","3"],["do","re","me"]]

for list_value in triples:
    for element in list_value:
        print(element,end=' ')
    print("I have just finished one of the inner loops!!")
print("Now I am outside both for loops!!")
