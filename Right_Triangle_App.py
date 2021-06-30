import math
print("Wellcome to the Right Triangle App")

first_legs=float(input("please enter  legs of the  Right Triangle "))

second_legs=float(input("Please enter the hypotenuse of the Right Triangle "))

are_triangle=(first_legs*second_legs)*1/2

hypotenuse=math.sqrt((first_legs**2)+(second_legs**2))
perimetr=hypotenuse+first_legs+second_legs

print("Right Triangles Area is "+str(are_triangle))
print("Right Triangles Hypotenuse is "+str(hypotenuse))
print("Right Triangles Perimetr is "+str(perimetr))
                 
