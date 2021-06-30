print("Function Global variable ")

def remove_names(names):
    removed_names=names.pop()
    print("Goodbye ",removed_names.title(),".")
    return names

friends=['jhon','jill','james']

#print(friends)
new_friends=remove_names(friends.copy())
print(friends)
print(new_friends)




"""def add_two(num):
    num+=2
    return num 

value=10
print(value)
value=add_two(value)
print(value)
#print(value)"""

"""
nums=[1,2,3,4,5]
new_nums=nums[:] # nums.copy()
new_nums.append(6)
print(nums)
"""
print()
