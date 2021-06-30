print("Wellcome to the Letter Cunter App")
name=str(input("What is your name ? ")).title()
print("Hello !" + name)
sentence=str(input("Please write your sentence "))
letter = str(input("Which letter would you find ? " ))
letter=letter.lower()
sentence=sentence.lower()

letter_count = sentence.count(letter)
print(letter_count)

print("\n" + name + ", your message has " + str(letter_count) + " " + letter +
"'s in it.")


