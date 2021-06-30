print("Introdiction Functions")

#print("Hello")
#name=input("Enter your Name ")
#age=int(input("Enter your ages "))

def hello_word(name,age):
    """Great the whole world"""
    print("Hello world",name.title())
    print("You are ",age," years old.")

hello_word("narmin",22)
print()
user_name='mike'
user_age=33
hello_word(user_name,user_age)

print()
def goodbye_world(name='nobady',day='today'):
    """Say goodbye"""
    print("Goodbye ",name.title()," ... ")
    print("May you have a good ",day.title()," .")
goodbye_world()
print()
goodbye_world("Mike")
print()
goodbye_world("mike",'friday')

print()


def calc_age(age=0,interval=10):
    """Calculate a persons age in x years"""
    print("You are ",age," years old")
    age+=interval
    print("In",interval," years you will be ",age,".")

calc_age(33)
print()
calc_age(33,22)
# Return Values

print()
print("Return Values ")
def calc_age(age,interval=0):
    """Determine aa persons age a interval years."""
    age+=interval
    return age

new_age=calc_age(30,10)
print(new_age)



def course_info(course_name,student_number,credit_hours):
    """Simulate a college course and return the summary as a dict"""
    course={
        'Course Name':course_name.title(),
        'Student Number':student_number,
        'Credit Hours': credit_hours,
        }
    return course
python=course_info("Python programming",32,4)
# print(type(python)) for checking is it dictionary or not ? 

for key ,value in python.items():
    print(key," : ",value)

def drop_student(course):
    course['Studen Number']-=1
    print("Dropping student from ",course["Course_Name"])

drop_student(python)



































    
































































    
    
