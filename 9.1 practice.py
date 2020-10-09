

def main():
    days_steps = {}
    total = 0
    minimum = 1000000
    maximum = 0
    for day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
        steps = int(input("Enter the total amount of steps for " + day + ": "))
        days_steps[day] = steps
        if steps > maximum:
            maximum = steps
        if steps < minimum:
            minimum = steps
        total += steps
    average = total/7
    print("You walked a total of " + format(total, '.0f') + " steps this week")
    print("Your average amount of steps was " + format(average, '.0f'))
    print("The maximum steps you took were " + str(maximum) + " on ")
    for days in days_steps:
        if days_steps[days] == maximum:
            print("\t" + days)
    print("The minimum steps you took were " + str(minimum) + " on ")
    for days in days_steps:
        if days_steps[days] == minimum:
            print("\t" + days)


main()
