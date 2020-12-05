

import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        input_file = open("customer_file.dat", 'rb')
        customers = pickle.load(input_file)
        print(customers)
    except (FileNotFoundError, IOError):
        print("File not found, please add a customer then quit to create the file.")
        customers = {}
    choice = 0

    while choice != QUIT:
        choice = menu()

        if choice == LOOK_UP:
            look_up(customers)
        elif choice == ADD:
            add(customers)
        elif choice == CHANGE:
            change(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            save(customers)


def menu():
    print("Customer email lookup")
    print("---------------------")
    print("1. Look up a customer")
    print("2. Add a customer")
    print("3. Change an email")
    print("4. Delete a customer")
    print("5. Save and Quit\n")

    choice = int(input("Enter the number of your choice: "))
    while choice < 1 or choice > 5:
        choice = int(input("Enter a valid choice: "))
    return choice


def look_up(customers):
    name = input("Enter a customer name: ")
    print(customers.get(name, 'Not found'))


def add(customers):
    name = input("Enter a customer name: ")
    email = input("Enter a customer email: ")
    if name not in customers:
        customers[name] = email
    else:
        print("That already exists.")


def change(customers):
    name = input("Enter a customer name: ")
    if name in customers:
        email = input("Enter a new email: ")
        customers[name] = email
    else:
        print("Not found.")


def delete(customers):
    name = input("Enter a customer name")
    if name in customers:
        del customers[name]
    else:
        print("Not found.")


def save(customers):
    print("The data has been saved to a file.")
    save_file = open('customer_file.dat', 'wb')
    pickle.dump(customers, save_file)
    save_file.close()


main()


