pi = 3.14
print("This program tells you the area of a shape")


def main():
    choice = 0
    good_choice = validate(choice)
    rectangle(good_choice)
    triangle(good_choice)
    square(good_choice)
    circle(good_choice)


def validate(choice):
    while choice < 5:
        print(" 1. Rectangle\n 2. Triangle\n 3. Square\n 4. Circle\n 5. Quit")
        choice = int(input("Pick a number: "))

        if choice > 4:
            print("Goodbye")
        else:
            print("You picked", str(choice))
        return choice


def rectangle(choice):
    if choice == 1:
        width = int(input("Enter a width "))
        length = int(input("enter a length "))
        print("The area is ", length * width)


def triangle(choice):
    if choice == 2:
        base = int(input("What is the base "))
        height = int(input("What is the height "))
        print("The area is ", (base * height) / 2)


def square(choice):
    if choice == 3:
        length = int(input("Enter the length or width "))
        print("The area is ", length * length)


def circle(choice):
    if choice == 4:
        radius = int(input("What is the radius "))
        print("The area is ", pi * (radius * radius))


main()
