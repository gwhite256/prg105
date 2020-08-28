# This program determines if a student is applicable for financial aid

# Declare the boolean value
financial_aid_status = True

# Get the data from the user
student_status = input("Are you a new or returning student? Enter R or N: ")
if student_status != 'R' or student_status == 'N':
    financial_aid_status = False
gpa = float(input("What is your GPA: "))
if gpa < 2.0:
    financial_aid_status = False
criminal_record = input("Have you been convicted of a drug related crime? enter Y or N ")
if criminal_record == 'Y':
    financial_aid_status = False
credit_hours = int(input("How many credit hours are you enrolled in: "))
if credit_hours < 6:
    financial_aid_status = False
yearly_income = int(input("What is your yearly income: "))
if yearly_income > 50000:
    financial_aid_status = False

# Display the boolean status as an output to the user
if financial_aid_status:
    print("You are eligible for financial aid.")
else:
    print("You are not eligible for financial aid.")
