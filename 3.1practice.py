# This program determines if a student is applicable for financial aid

# Qualifications
GPA_Status = 2.0
Credit_Hours = 6.0
Minimum_Salary = 50000

# Get students information

GPA = float(input('Enter your GPA: '))
Hours = float(input('How many credit hours are you enrolled: '))
Salary = int(input('What is your yearly income: '))
Status = input('Are you a new or returning student: ')
Felony = input('Have you ever been convicted of a drug related crime: ')

# Output if statements

if GPA >= GPA_Status:
    if Hours >= Credit_Hours:
        if Salary <= Minimum_Salary:
            if Status == "r" or "n":
                if Felony == "n":
                    print("You qualify for financial aid.")
                else:
                    print("You do not qualify for financial aid.")
