

def main():
    line = []
    student_grade = []
    count = int(input("How many students do you need to enter data for?: "))
    for student in range(0, count):
        name = input("Enter the students name: ")
        grade = input("Enter the students grade: ")
        line.append(name)
        line.append(grade)
        student_grade.append(line)
        line = []
    print(student_grade)

    outfile = open("student_grade.txt", "w")
    for line in student_grade:
        line_out = "'" + line[0] + "' , '" + line[1] + "'\n"
        outfile.writelines(line_out)
    outfile.close()


main()
