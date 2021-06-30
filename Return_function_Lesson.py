print("Return function")



def calc_age(age,interval=0):
    """Determine a persons age after interval years."""
    age+=interval
    return age

new_age=calc_age(43,23)
print(new_age)
print("--------------------------")

def course_info(course_name,student_number,credit_hours):
    """ Simluate a college course and return the summary as a dict"""
    course={
        'Course Name': course_name.title(),
        'Student Number':student_number,
        'Credit Hours':credit_hours,
        }
    return course


    

python=course_info("Python programmming",32,4)

for key ,value in python.items():
    print(key," : ",str(value))

# Dropping a student from course 
def drop_student(course):
    """Simulate dropping a student from a specific course """
    course['Student Number']-=1
    print("Dropping student from  ",course['Course Name']," .")


drop_student(python)

for key,value in python.items():
    print(key," : ",str(value))

















