

def main():
    sales_total = open("sales_totals.txt", 'r')

    line = sales_total.readline

    while line != '':
        amount = float(line)

        print(format(amount), '.2f')

        line = sales_total.readline


main()
