print("Welcome to the Database  Admin Program .My Own Algorithm ")

log_on_information={
    "mooman74":"alskes145",
    "meramo1986":"kehns0101",
    "nickyD": "world1star",
    "george2":"booo3oha",
    "admin00":"admin1234",
    }

username=input("Enter your username :")
password=input("Enter your password : ")

#for username,passwords in log_on_information.items():
     #print(username)
     #for password in log_on_information.values#
    #print('\t',password.title())

if username=="admin00" and password=="admin1234":
    for usernames,passwords in log_on_information.items():
        print('\n'"Usernames are : ",usernames,'\t'" Password are :",passwords)
        #for password in log_on_information.values():
            #print(password)

elif username in log_on_information.keys() and password in log_on_information.values():
    print("Hello ",username ,"! ","You are logged in ")
    choice=input("Would you lik to change your password (yes/no):").lower().strip()

   


    if choice=='yes':
       changed_password=input("What would you like your new password to be :").lower().strip()

       if len(changed_password)<8:
        print(changed_password,"not the minimum eight characters")
        
       elif len(changed_password)==8:
        log_on_information['username']=changed_password
        print("Your password has already changed ",username,"your password is",changed_password)
       else:
           print("So long password ")
    else:
        print("Your password has not changed ")
    

    
else:
    print("Username not in database , goodbye ")
    
