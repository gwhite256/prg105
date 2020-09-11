

def main():
    num = int(input("Enter a number between 20 and 100: "))
    validate(num)
    check_two(num)
    check_three(num)
    check_five(num)


def validate(num):
    if num >= 20 or num <= 100:
        print("Your number is ", num)
    else:
        print("Enter a valid number")
    return num


def check_two(num):
    if num == (num // 2) % 0:
        print(num, " Is divisible by 2")
    else:
        print(num, " Is not divisible by 2")
    return num


def check_three(num):
    if num == (num // 2) % 0:
        print(num, " Is divisible by 3")
    else:
        print(num, " Is not divisible by 3")
    return num


def check_five(num):
    if num == (num // 2) % 0:
        print(num, " Is divisible by 5")
    else:
        print(num, " Is not divisible by 5")


main()
