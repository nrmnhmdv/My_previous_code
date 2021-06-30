print("Wellcome to the Different Types of Lists Program")
print()
print('\t\t'"Summary Table")
num_string=['13','189','67','100']

print("The variable num_strins is a",type(num_string))
print("It contains the elements : ",num_string)
print("The element",num_string[0],"is a",type(num_string[0]))

print()
num_int=[13,87,90,4,878,54,0]
print("The variable num_int is a",type(num_int))
print("It contains the elements :",num_int)
print("The element",num_int[0],"is a",type(num_int[0]))

print()
float_list=[10.9,90.9,4.5,6.7,7.8,999.9999]

print("The variable float_list is a",type(float_list))
print("It contains the elements :",float_list)
print("The element",float_list[0],"is a",type(float_list[0]))


print()
list_list=[[1,2,3],[4,6,5],[0,9,10]]
print("The variable list_list  is a ", type(list_list))
print("It contains the elements ",list_list)
print("The element",list_list[0]," is a",type(list_list[0]))

print()

print("Now sorting num_strings and num_int ")
print("Sorted num_string : ",sorted(num_string))
print("Sorted num_int :" , sorted(num_int))
## niye bele olanda cixmir amma bele olanda cixir baxmaq lazimdir

num_int.sort()
#print(num_int)
print("\nStrings are sorted alphabetically while integers are sorted numerically!!!")





