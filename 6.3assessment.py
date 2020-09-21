

def main():
    total = 0
    count = 0
    file_name = "sales_error.txt"
    line = 0
    try:
        in_file = open("sales_error.txt", 'r')
        for line in in_file:
            sales_amt = float(line.rstrip('\n'))
            print(format(sales_amt, '10,.2f'))
            total += sales_amt
            count += 1
    except IOError:
        print("Cannot read file:" + file_name)
    except ValueError:
        print("This value is not acceptable " + line)
    print("Total: " + format(total, "23,.2f"))
    print("Count:" + format(count, "19,.2f"))
    print("Average of numbers: " + format(total/count, '2.2f'))


main()
