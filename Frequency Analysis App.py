from collections import Counter 
print("Frequency Analysis App")

#phrase=input("Please enter any phrase ")

#list of elements to remove from all text for analysis
non_letters=['1','2','3','4','5','6','7','8','9','0',' ','.',',','?','"','"',':',';','(',')','%','$','&','#','\n','\t','!']
 #information for the first key key_phrase_1
key_phrase_1=input("Enter a word or phrase to count the occurence of each letter :").lower().strip()

#removing all non letters from key_phrase_1
for non_letter in non_letters:
    key_phrase_1=key_phrase_1.replace(non_letter,'')

#print(key_phrase_1)

total_occurences=len(key_phrase_1)

# Create a counter object to tally the number of each letter

letter_count=Counter(key_phrase_1)
#print(letter_count)

print("\n Here is the frequency analysis from key phrase 1 : ")
print("\n\t Letter\t\tOccurrence\t\tPercentage ")

for key,value in sorted(letter_count.items()):
    percentage=100*value/total_occurences
    
    percentage=round(percentage,2)
    print("\t",key,"\t\t\t\t",value,"\t\t\t",percentage,"%")


#Make a list of letters from highest occurence
order_latter_count = letter_count.most_common()
key_phrase_1_ordered_letters=[]

for pair in order_latter_count:
    key_phrase_1_ordered_letters.append(pair[0])

#Print the list
for letter in key_phrase_1_ordered_letters:
    print(letter,end='')


# Second phrase

key_phrase_2 = input("\nEnter a word or phrase to count the occurence of each letter :").lower().strip()

# removing all non letters from key_phrase_1
for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, '')

# print(key_phrase_1)

total_occurences = len(key_phrase_2)

# Create a counter object to tally the number of each letter

letter_count = Counter(key_phrase_2)
# print(letter_count)

print("\n Here is the frequency analysis from key phrase 2 : ")
print("\n\t Letter\t\tOccurrence\t\tPercentage ")

for key, value in sorted(letter_count.items()):
    percentage = 100 * value / total_occurences

    percentage = round(percentage, 2)
    print("\t", key, "\t\t\t\t", value, "\t\t\t", percentage, "%")

# Make a list of letters from highest occurence
order_latter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []

for pair in order_latter_count:
    key_phrase_2_ordered_letters.append(pair[0])

# Print the list
for letter in key_phrase_2_ordered_letters:
    print(letter, end='')





















    


