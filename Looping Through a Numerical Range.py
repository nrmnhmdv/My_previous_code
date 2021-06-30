print("Looping Through a Numerical Range")

values=range(1,10)
print(values)
print(type(values))

for i in range(1,10):
    print(i)

print()
for num in range(5):
    print(num)

for i in  range(2,11,2):
    print(i,end=' ')
print()
word="Hello World"
list_word=list(word)
print(word)
print(list_word)
list_word[5]="NEW" # space nin yerine NEW sozunu yazdirdi
print(list_word)
new_word="hi".join(list_word) # join etdi her araliga
#print(list_word," it is thrid ")
print(new_word)

print()
numbers=list(range(10,110,10))

print(numbers)

for number in numbers:
    print(number)


squares=[]
for number in numbers:
    square=number**2
    squares.append(square)
print(squares)
print("Populating squares comlpete ")
print()
for square in squares:
    print(square)
print("Hello World!!!!!!!!")
cubes=[number**3 for number in numbers]
for cube in cubes:
    print(cube)

print()
print(max(cubes))
print(min(cubes))
print(sum(cubes))