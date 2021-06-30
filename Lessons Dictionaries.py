print("Lessons Dictionaries ")

bob_info={
    "first_name":"Bob",
    "last_name ":"Honda",
    "age":21,
    "fav_color":['green','orange']}
print(bob_info)
print(type(bob_info))
print(bob_info['age'])
print(bob_info['fav_color'][0])

bob_info['weight']=180
bob_info['height']=72.6
print(bob_info)
bob_info['weight']-=5
print(bob_info["first_name"],"Wow you lost some weight ",bob_info['weight'])

bob_info['age']+=1
print("Happy Brithday ",bob_info["first_name"]," ",bob_info["age"])
# delet key from dictionary
del bob_info['fav_color']
print(bob_info)
user_info={}
user_info['name']=input("What is your name ?").title()
user_info['age']=int(input("What is your age ?"))
user_info['job']=input("What is your job ?").title()

print(user_info)