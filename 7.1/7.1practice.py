line = 0

total_students = int(input("How many students are you entering into the system?: "))
student_grades = []
outfile = open("student_grade.txt", "w")

for line in student_grades:
    name = input("Enter the students name: ")
    grade = input("Enter the students grade: ")
    line_out = "'" + line[0] + "' , '" + line[1] + "'\n"
    outfile.writelines(line_out)
outfile.close()
