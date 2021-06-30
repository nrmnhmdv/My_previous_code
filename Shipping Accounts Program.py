print("welcome to the Shipping Accounts Program")

users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']
username=input("Hello ,  what is your username :")


if username in users:
    print("\nHello " + username + ". Welcome back to your account.")
    print("Current shipping prices are as follows:")
    print("\nShipping orders 0 to 100: \t\t$5.10 each")
    print("Shipping orders 100 to 500: \t\t$5.00 each")
    print("Shipping orders 500 to 1000: \t\t$4.95 each")
    print("Shipping orders over 1000: \t\t$4.80 each")

    quantity=int(input("How many items would you like to ship :"))
    if quantity<100:
        cost=5.10
    elif quantity<500:
        cost=5.00
    elif quantity<100:
        cost=4.95
    else:
        cost=4.00

    bill=quantity*cost
    bill=round(bill,2)

    print("To ship " + str(quantity) + " items it will cost you $" + str(bill) +" at $" + str(cost) + " per item.")
    choice = input("\nWould you like to place this order (y/n): ").lower()
    if choice.startswith('y'):
        print("Okay. Shipping your " + str(quantity) + " items.")
    else:
        print("Okay, no order is being placed at this time.")
else:
    print("So sorry , you do not have account in ours application ")
