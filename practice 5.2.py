

def main():
    num = int(input("Enter a number between 20 and 100: "))
    good_num = validate(num)
    two = check_two(good_num)
    three = check_three(good_num)
    five = check_five(good_num)
    output(good_num, two, three, five)


def validate(num):
    if 20 <= num <= 100:
        return num
    else:
        while num < 20 or num > 100:
            print("That is not a valid number.")
            num = int(input("Enter a number between 20 and 100: "))
    return num


def check_two(num):
    if num % 2 == 0:
        return " is divisible by 2."
    else:
        return " is not divisible by 2."


def check_three(num):
    if num % 3 == 0:
        return " is divisible by 3."
    else:
        return " is not divisible by 3"


def check_five(num):
    if num % 5 == 0:
        return " is divisible by 5."
    else:
        return " is not divisible by 5."


def output(num, two, three, five):
    print(str(num) + two)
    print(str(num) + three)
    print(str(num) + five)


main()
