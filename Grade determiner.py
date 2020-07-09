# Welcome to grade calculator.
#This program helps one to calculate his/ her gpa for a semester.
# All you just do is follow the prompt and question and you will be fine.

# created a function that takes in the number of courses the user takes a in a semester.
def Courses_taken_sem():

# created a variable called "no_course" to accept the number of courses the individual took that semester.
    no_Course= int(input("How many courses did you take this semester"))

# created a dictionary and assigned to store the course name as the key, the credit hours and the and the grade the aquired in the subject as the values in a list.
    names_courses=dict()

# istantiated a for loop to with variables that store the name, grade aquired and the credit hours.
    for num in range(no_Course):
        Courses_name=input("Enter CourseName: ")
        Course_grade=input("Enter the "+ Courses_name+" (s) Grade: ")
        Course_credithours=eval(input("Enter " +Courses_name +" ('s) credit-hours: "))

# here i task the dictionary i created to add the values to a course-name provided the course name does has not been already added to the dictionary. 
        names_courses.setdefault(Courses_name,[])
        names_courses[Courses_name].append(Course_grade.upper())
        names_courses[Courses_name].append(Course_credithours)
    return names_courses
# Here i created a function to calculate the total gpa score per the information given. 
def grade_allocation():

# use the dictionary class to store the the set down grade_gpa allocations for the school.
    grade_allct= {"A+":4.00,"A":4.0,"B+":3.5,"B":3.0,"C+":2.5,"C":2.0,"D+":1.5,"D":1.0}
    cum_la_Score=0
    names_courses=Courses_taken_sem()

# create a two for loops to loop through the dictionary and it values to get the total gpa per the grade allocation.
    for grade in names_courses :
        for grade_score in grade_allct:
            list_det=names_courses.get(grade)
            if list_det[0] ==grade_score:
                cum_la_Score=cum_la_Score+float(grade_allct.get(grade_score))
    print(cum_la_Score)
    return cum_la_Score, names_courses

# Here i created a function to calculate the overall gpa score for depending on the credit hours provided by the user.
def cum_la_gpa_score():
    cum_la_Score,names_courses=grade_allocation()
    credith_total=0
# created a for loop to  get the courses-credits pers the user.
    for course in names_courses:
        list_det1=names_courses.get(course)
        credith_total=credith_total+float(list_det1[1])
    gpa_score=cum_la_Score/credith_total
    return cum_la_Score,names_courses,gpa_score

# created a function to print out the introduction, the Courses taken together with the credit hours and the grade. and finally your gpa score for the semster.   
def Information():
    intro= """ Hello and welcome to the "\Gpa calculator"\
Gpa Calculator is used to calculate your Gpa for a semester
All you need to do is follow the prompts and u should be fine"""
    print(intro)
    print(" ")
    try:
        cum_la_Score,names_courses,gpa_score=cum_la_gpa_score()
    except:
        ZeroDivisionError
        cum_la_Score,names_courses,gpa_score=cum_la_gpa_score()
    print( "Courses you took this semester :\n",names_courses)
    print("Gpa Score for the Semester: " ,gpa_score)
Information()  
    
        
        
