#print("Lesson about Class")
import random

class Baby():
    """ """
    def __init__(self,name,gender,age):
        """ Initialize attributes """
        self.name=name.title()
        self.gender=gender
        self.age=age

        self.tired=True

    def play(self):
        """Simulate playing based on gender  """
        
        if self.gender=='male':
            print(self.name+" is playing with cars")
        else:
            print(self.name,"is playing with doll") 

    def cry(self):
        """ Simulate  Crying """
        
        print("WAAAH WAAAH WAHHHH!!!!")
        print("Even ",self.age," year olds cry ")

    def sleep(self):
        """ Simulate Sleeping"""
        
        if self.tired:
            print(self.name,"is sleeping...FINALLY")
            self.tired=False
        else:
            print("So Sorry !! ",self.name," is not tired ")
            


little_boy=Baby('Jhon','male',3)
little_gril=Baby('Karla','female',2)


print("Name is ",little_boy.name, " ",little_boy.age," years old")
print("Name is ",little_gril.name,"",little_gril.age," years old")



little_boy.play()
little_gril.play()

little_gril.cry()
little_boy.cry()

little_boy.sleep()
little_gril.sleep()

print("\nCreate more Baby classes ")

babies=[]

for i in  range(25):
    num=random.randint(0,1)
    if num==0:
        gender='male'
    else:
        gender='female'

    age=random.randint(0,5)

    baby=Baby("Sam",gender,age)
    babies.append(baby)

for baby in babies:
    print(baby.name," is a ", baby.age," year old",baby.gender,".")

    





















    
        















