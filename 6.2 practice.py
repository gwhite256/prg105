

def main():
    sales_total = open("sales_totals.txt", 'r')
    total = 0
    count = 0
    for line in sales_total:
        sales_amt = float(line.rstrip('\n'))
        print(format(sales_amt, '10,.2f'))
        total += sales_amt
        count += 1
    print("Total: " + format(total, "23,.2f"))
    print("Count:" + format(count, "19,.2f"))
    print("Average of numbers: " + format(total/count, '2.2f'))


main()
