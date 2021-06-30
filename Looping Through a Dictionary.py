print("Lesson Through a Dictionary ")
#looping tg
fav_color={
    'john':"blue",
    'gabe':"orange",
    'mary':"yellow",
    'mike':"purple",
    "lucas":"pink",
    "sarah":"yellow"}

print(fav_color)

print(fav_color['sarah'])
print(fav_color['lucas'])

fav_color_list=fav_color.items()
print(fav_color_list)

print()
for key ,value in fav_color.items():
    print("The key "+key.title()+" has an associated value of "+value.title()+" . ")


print()
fav_color_keys=fav_color.keys()
print(fav_color_keys)

print()
for name in fav_color_keys:
    print(name.title()," thank you for taking the survey")

print("----------------------------------------")
if 'brooke ' not in fav_color.keys():
    print(" Brooke you should take the survey !!!!")


print()
fav_colors_values=fav_color.values()
print(fav_colors_values)

print("--------------------------")
for color in fav_colors_values:
    print(color.title())

print()
print("Using Set function ")
for value in set(fav_colors_values):
    print(value.title())























