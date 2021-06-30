# nesting Dictionary
print("Welcome to the Complex Dictionary Structure ")


user_0={
    'name':'john',
    'age':22,
    }

user_1={
    'name':'bill',
    'age':27,
    }

user_2={
    'name':'mary',
    'age':32,
    }
users =[user_0,user_1,user_2]

for user in users:
    print(user)

print("---------------------------------------------")
for user in users:
    for key , value in user.items():
        print(key.title(),"\t",value)
    print('\n')


friends={
    'bill':['john','tom','mary'],
    'tom':['john','bill','sue'],
    'mary':['sue','bill','tom'],
    }

for key,values in friends.items():
    print('\n',key.title(),"'s friends are :")
    for value in values:
        print('\t',value.title())
print('\n')

user_directory={
    'msmith':{
        'first_name':'mark',
        'last_name':'smith',
        'age':27,
        },
    'ejones':{
        'first_name':'eddie',
        'last_name':'jones',
        'age':24,
        },
    }
for user , info in user_directory.items():
    print('\t'"Username : ",user)
    for  key , value in  info.items() :
        print('\t',key," ",value)
    













        
