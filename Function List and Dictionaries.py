print("Lits and Dictionaries")

def remove_name(names):
    """ Remove a name from a list """
    removed_name=names.pop()
    print("Godbye ",removed_name.title()," .")

friends=['john','jack','jill','james']
print(friends)
remove_name(friends)
