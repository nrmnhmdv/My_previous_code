print(" Welcome to the Binary and Hexadecimal Coversation App")
max_value = int(input("Compute binary and hexadecimal values up to the following decimal number "))


decimal=list(range(1,max_value+1))

binary=[]
hexadecimal=[]

for num in decimal:
    binary.append(bin(num))
    hexadecimal.append(hex(num))
    
print("Generating lists .... complete !")

print("Using slices, we will now show a portion of each list")
low_range=int(input("What decimal would you like to start at :"))
high_range=int(input("What decimal would you like to stop at :"))

print("Decimal values from",low_range," to ",high_range)
for deci in decimal[low_range-1:high_range]:
    print(deci)

print()

print("Binary values from ",low_range," to ",high_range)

for binar in binary[low_range-1:high_range]:
    print(binar)

print()
print("Hexadecimal values from ",low_range," to ",high_range )

for hexa in hexadecimal[low_range : high_range]:
    print(hexa)




print("\nPress Enter to see all values from 1 to "+str(max_value)+".")
print("Decimal----Binary----Hexadecimal")
print("----------------------------------------------")
for d, b, h in zip(decimal, binary, hexadecimal):
    print(str(d) + "----" + str(b) + "----" + str(h))



















