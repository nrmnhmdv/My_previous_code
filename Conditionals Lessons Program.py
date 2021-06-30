print("Welcome to the Conditionals Lessons ")
#boolean value

status =True
print(status)
print(type(status))

print()
status=False
print(status)
print(type(status))


# = assignment operator
## == comparison operator
print("Assigment or Comparison ")
soda='coke'
print(soda=='coke')

print(soda=='cola')
print("Lowercase and letters are not equal")
print(soda=="Coke")
print(soda != 'root beer')

names=["mike ",'john','mary']

print("Check List  : ")
mike_status= 'mike ' in names
print(mike_status)

bill_status='bill ' not in names
print(bill_status)
