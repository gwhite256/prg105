print("Types of tickets and prices:")
print("1. Student $5.00")
print("2. Veteran $7.00")
print("3. Show Sponsor $2.00")
print("4. Retiree $6.00")
print("5. General Public $10.00")
student = 5
veteran = 7
sponsor = 2
retiree = 6
public = 10
customer_title = int(input("Enter a number for the category that fits you "))
total_tickets = int(input("How many tickets would you like? "))

if customer_title == 1:
    total_price = total_tickets * student
elif customer_title == 2:
    total_price = total_tickets * veteran
elif customer_title == 3:
    total_price = total_tickets * sponsor
elif customer_title == 4:
    total_price = total_tickets * retiree
elif customer_title == 5:
    total_price = total_tickets * public
else:
    total_price = total_tickets * public

if total_tickets <= 8:
    discount = total_price * .1
elif total_tickets <= 15:
    discount = total_price * .15
elif total_tickets > 15:
    discount = total_price * .2
else:
    discount = 0

if total_price == total_tickets * student:
    ticket = (total_price - discount) / total_tickets
elif total_price == total_tickets * veteran:
    ticket = (total_price - discount) / total_tickets
elif total_price == total_tickets * sponsor:
    ticket = (total_price - discount) / total_tickets
elif total_price == total_tickets * retiree:
    ticket = (total_price - discount) / total_tickets
elif total_price == total_tickets * public:
    ticket = (total_price - discount) / total_tickets
else:
    ticket = 0

print('Your total before discounts is: $',
      format(total_price, '.2f'))
print("Your total after discounts is: $",
      format(total_price - discount, '.2f'))
print("The price per ticket was: $",
      format(ticket, '.2f'))
