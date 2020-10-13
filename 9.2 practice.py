

def main():
    correct = 0
    print("This is a test to see how well you know your spanish numbers.")
    numbers = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'quatro', 'five': 'cinco', 'six': 'seis',
               'seven': 'siete', 'eight': 'ocho', 'nine': 'nueve', 'ten': 'diez'}
    for value in numbers:
        answer = input("How do you say " + value + ' in spanish: ')
        answer = answer.lower()
        if numbers[value] == answer:
            print("Correct\n")
            correct += 1
        else:
            print("That was wrong")
            print("The right answer was: " + numbers[value] + "\n")
    print("You got " + str(correct) + " correct")
    if correct == 10 or correct == 9:
        print("Grade: A")
    elif correct == 8:
        print("Grade: B")
    elif correct == 7:
        print("Grade: C")
    elif correct == 6:
        print("Grade: D")
    else:
        print("Grade: F")


main()
