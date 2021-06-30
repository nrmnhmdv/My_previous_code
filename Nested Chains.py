print("Welcome to the Nested if elif else Chains ")

## [], "" value is False

our_list=[2]
our_string="a"


if our_list:
    print("This list has something in it ")


if our_string:
    print("Our string is not empty !!")
print("------------------------------------")

teams=["knicks","kings","heat","pacers","pelicans","celics"]

for team in teams:
    if team.startswith('k'):
        print("The "+team.title()+" Could win the NBA ")
        if team=='knicks':
            print('\n'"I know they will win !!")
        else:
            print("They probably won not  though ....")
            
    elif team.startswith('p'):
        print('\n'"The ",team.title(),"will probably  make the play offs")
        if team=='pacers':
            print("They need Reggie Miller back though ")
    else:
        print("The ",team.title()," stands no chance this year")
