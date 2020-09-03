print("This program calculates how much"
      "you made in sales per week"
      "and gives you average sales per day")
total = 0
for day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
    sales = float(input("What were your total sales for " + day + ": "))
    total += sales
print("The total amount for sales this week was: ", format(total, '.2f'))
print("The average sales amount per day was: ", format((total / 7), '.2f'))
