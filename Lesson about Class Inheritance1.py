print("Inheritance")


#Interitance
#Parent class---> Child class

# The Parent class 
class Dog():
    """ A class to represent a general dog """

    def __init__(self,name,gender,age,loud):
        """Initilize attributes  """

        self.name=name
        self.gender=gender
        self.age=age
        self.is_loud=loud  # loud is a Bool

    def call_dog(self):
        """Call the dog"""
        if self.gender=='male':
            print("Here",self.name,'Good Boy!')
        else:
            print("Here ",self.name,'Good Gril')


    def dog_years(self):
        """Compute age in dog years """

        dog_years=self.age
        print(self.name,"is",dog_years,"years old")



    def bark(self):
        if self.is_loud:
            print("WOOF WOOF WOOF")
        else:
            print("woof")


# A child class Beagle

class Beagle(Dog):
    """ A class to represent a specific type of dog """

    def __init__(self,name,gender,age,loud,gunshy):
        """ Initilize attributes of the parent class """

        super().__init__(name,gender,age,loud)
        self.gunshy=gunshy # Bool

    # Overwritten 
    def bark(self):
        if self.is_loud:
            print("HoWLLLLLL")
        else:
            print("Howw")
            
    def go_hunt(self):
        """ If the dog is not a gunshy """
        if not self.gunshy:
            self.bark()
            print(self.name+' just brought back a duck.')
        else:
            print(self.name+'is not a good hunting dog.')
        
        
class Chihuahua(Dog):
    """ Represents a specific type of dog """
    def __init__(self,name,gender,age,loud):
        """ """
        super().__init__(name,gender,age,loud)

    def bark(self):
        if self.is_loud:
            print("YIP YIP YIP YIP")
        else:
            print("yip")


my_dog=Dog('Lilia','female',3,True)

print(my_dog.name)
print(my_dog.is_loud)
print(my_dog.age)

my_dog.dog_years()
my_dog.bark()

your_dog=Beagle("Lassie",'male',8,False,False)

print(your_dog.name)

your_dog.dog_years()
your_dog.bark()
your_dog.call_dog()

your_dog.go_hunt()
#my_dog.go_hunt() don't have accses to this function 


tiny_dog=Chihuahua('tiny','male',2,True)
print('\n Chihuahua')
tiny_dog.call_dog()
tiny_dog.dog_years()
tiny_dog.bark()








































            
