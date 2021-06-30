print("List Using Slicing")

numbers=list(range(1,11))

for num in numbers:
    print(num)

print("\n Slicing")

for num in numbers[0:5]:
    print(num)

print()
list_num=[2,4,6,8,10,12,14,16,18]

for num in list_num[4:8]:  # it is index
    print(num, end=' ')
# copy list

new_list=list_num # bu listleri kopi etmek demek deyil bu eyni liste isare edir
print()
print(new_list)
print(list_num)

new_list=list_num[:]

list_num.pop()
print("After coping lists  I poped one element of the list_num ",list_num)
print("After coping lists nothing changed",new_list)

names=['Smith','Adam','Morqana','Morqan','Lucy','Marta','Martin','Colin']
new_names=names.copy()

print(names)
print(new_names)
names.pop()

print(names)
print(new_names)
new_names[0]=new_names[0].upper()
print(new_names)
