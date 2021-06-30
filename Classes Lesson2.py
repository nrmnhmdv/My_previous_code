print("Another Look at Classes Lesson 2")

class House():
    """ A class to model a house  that is for sale."""

    def __int__(self,style,sq_footage,year_built,price):
        """Initialize attributes """
        self.style=style
        self.sq_footage=sq_footage
        self.year_built=year_built
        self.price=price

        self.sold=False
        self.weeks_on_market=0

    def display_info(self):
        """Display the information on the house """
        print("\n ---- House for Sale------")
        print("House Style :\t",self.style)
        print("Square Feet :\t",self.sq_footage)
        print(" Year Built :\t",self.year_built)
        print("Sale Price :\t",self.price)
        print("\n This house has been on the market for ",self.weeks_on_market,"weeks")


    def sell_house(self):
        """ Sell the house !!! """
        if self.sold==False:
            print("Congraluations! Your house has sold for $ ",self.price)
            self.sold=True
        else:
            print("Sorry this house is no longer for sale")


    def change_price(self,amount):
        """Change the sale price of the house  """
        self.price+=amount
        if amount<0:
            print("Price drop!!")
        else:
            print("The house has inreased in value by $ ",amount ," . ")


    def update_weeks(self,weeks=1):
        """Increment the number of  """
        self.weeks_on_market+=weeks


my_house=House("Ranch",1800,1962,199000)

#Print out attributes
print(my_house.style)
print(my_house.sq_footage)
print(my_house.price)
print(my_house.sold)





























    









        
