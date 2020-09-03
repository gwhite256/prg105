print("This program calculates how much"
      "you made in sales per week"
      "and gives you average sales per day")
max_num = 7
total = 0
for counter in range(max_num):
    num1 = int(input("Enter the total sales for Monday: "))
    total = total + num1


print("The total sales this week were: ", total)
print("The average sales per day were:", total / 7)
