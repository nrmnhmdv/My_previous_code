def get_info():
    """Get user information to store in a dict that represents a bank account"""
    print("Welcome to the Python First National Bank ")
    #Get user input 
    name=input("Please enter your name ").title().strip()
    saving=int(input("How much money would you like to set up your savings account with: "))
    checking=int(input("How much money would you like to set up your checking account with: "))

    # build a dict that represents a specific bank account
    bank_account={
        'Name':name,
        'Saving':saving,
        'Checking':checking}
    return bank_account


def make_deposit(bank_account,account,money):
    """ Add money to a specific type of account """
    bank_account[account]+=money
    print("\nDeposited $  ",money," into ",bank_account['Name'],"'s",account.lower()," account" )
    


def make_withdrawal(bank_account,account,money):
    """ Withdraw money from a spesific type of account """
    # check that balance will still be positive after the withdraw
    if bank_account[account]-money>=0:
        bank_account[account]-=money
        print("\n Withdrew $",money," from ",bank_account['Name'],"'s",account.lower()," account ")
    # not enough money
    else:
        print("\n Sorry , by withdrawing $ ",money,"from",account," you will have a negative balance ")

        

def display_info(bank_account):
    """ Display all key-value pairs in a given bank account """
    print("\n Current Account Information")
    for key,value in bank_account.items():
        if key=='Name':
            print(key," : ",value)
        else :
            print(key," : $",value)


# The main code
# create a bank account
my_account=get_info()


running=True
while running:
    #Show the currrent state of the bank account
    display_info(my_account)

    #Get user input for the transaction
    account_type=input("\n What account would you like access (Saving or Checking):").title()
    choice=input("What type of transaction would you like make (deposit or withdrawal )")
    amount=float(input("How much money : "))

    # Make the correct function call based off previous user input
    if account_type=='Saving'or account_type=="Checking":

        if choice=="Deposit":
            make_deposit(my_account,account_type,amount)
        elif choice=="Withdrawal":
            make_withdrawal(my_account,account_type,amount)
        else:
            print("\n I'm sorry we can not do that for you today ")

    else:
        print("\n I'm sorry we can not do that for you today ")


    choice=input("Would you like to make another trasaction (y/n):").lower()
    if choice!='y':
        print("\n Thank you, Have a great day !")
        running = False























    















    
