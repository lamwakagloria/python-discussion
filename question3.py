#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail 
def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 50 <= score < 60:
        return 'E'
    else:
        return 'Fail'

def grade_students():
    
    while True:
        
        score = input("Enter the student's score (or type 'exit' to stop): ")
        
        if score.lower() == 'exit':
            break  
        
        try:
            score = float(score)  
            if 0 <= score <= 100:
                grade = calculate_grade(score)
                print(f"The student's grade is: {grade}")
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
grade_students()
