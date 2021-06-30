#Functions Challange : Loan Calculator App
from matplotlib import pyplot

def get_loan_info():
    """ Get teh basic information of a loan and store it in a dictionary """
    #Create a blank dict to represent a loan

    loan={}
    
    #Get user input for the categories of the loan
    
    loan['principal']=float(input("\n Enter the loan amount :"))
    loan['rate']=float(input("Enter the interest rate:"))/100
    loan['monthly payment']=float(input("Enter the desired monthly payment amount:"))
    loan['money paid']=0

    return loan



def show_loan_info(loan,number):
    """ Display the current loan status """
    print("\n---------Loan information",number," months ---------")
    for key,value in loan.items():
        print(key.title(),":",value)

        

def collect_interest(loan):
    """ Update  loan for interest per month  """
    # Divide by 12 to simulate collecting inteterst monthly
    loan['principal']=loan['principal']+loan['principal']*loan['rate']/12


def  make_monthly_payment(loan):
    """Simulate making a monthly payment to pay down the principal """
    loan['principal']=loan['principal']-loan['monthly payment']
#You are required to make a full pament this month
    if loan['principal']>0:
        loan['money paid']+=loan['monthly payment']
#You are not required to make a full payment this month
    else:
        # For this else block loan[principal] will be negative
        loan['money paid']+=loan['monthly payment']+loan['principal']
        loan['principal']=0        





def summarize_loan(loan,number,initial_principal):
    """Display the results of paying off the loan """
    print("\n Conguraulations! You paid off your loan in",number," month!")
    print("Your initial loan was $",initial_principal," at a rate of",100*loan['rate']," % ")
    print("Your monthly payment was $ ",loan['monthly payment'],".")
    print("You spent $",round(loan['money paid'],2),"in total")

    # Calculate money spent on interest 
    interest=round(loan['money paid']-initial_principal,2)
    print()



def crate_graph(data,loan):
    """create a graph to show the relationship between principal and time """
    
    x_values=[] # These represent month numbers
    y_values=[] #  Tehese represent corresponding  princiapl value
    # Loop Through data set. Point is a tuple
    #point[0] represents a month number, point[1]
    for point in data:
        x_values.append(point[0])
        y_values.apppend(point[1])
    # Create a plot for x values and y values
    pyplot.plot(x_values,y_values)
    pyplot.title(str(100*loan['rate'])+"% Interest With $ ",str(loan['monthly payment']),"Monthly Payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")

    #Display the created graph
    pyplot.show()



#The main code


print("Welcome to the Loan Calculator App ")

#Initial variables
month_number=0

#Build a loan for the program
my_loan=get_loan_info()
starting_principal=my_loan['principal']
data_to_plot=[]

show_loan_info(my_loan,month_number)
input("Press 'Enter '  to begin  paying off your loan" )
#Simulate paying off the loan as long as the loan's principal>0

while my_loan['principal']>0:
    #You cannot get ahead of the interest, you will never pay off the loan so
    if my_loan['principal']>starting_principal:
        break
    #It is possible to pay off the loan so simulate a single month
    #Increment month number, collect interest make a payment add data to 
    month_number+=1
    collect_interest(my_loan)
    make_monthly_payment(my_loan)
    data_to_plot.append(month_number,my_loan['principal'])
    show_loan_info(my_loan,month_number)

# The loan is either paid off in fulll or it can NEVER be paid off....

if my_loan['principal']<=0:
    summerize_loan(my_loan,month_number,starting_principal)
    create_graph(data_toplot,my_loan)

# The loan can NEVER be paid off, can't
else:
    print("\n You will NEVER pay off your loan!!!!!")
    print("You cannot get ahead of the interest :(( ")
    











































    
