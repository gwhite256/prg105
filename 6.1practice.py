

def main():
    num_people = int(input("How many people are you entering into the system?: "))

    contact_list = open('people.txt', 'w')

    for count in range(1, num_people + 1):
        print('Enter information for person # ', count)
        name = input('Name, first and last:')
        email = input('Email ')
        phone = input('Phone Number: ')

        contact_list.write(name + str(','))
        contact_list.write(email + str(','))
        contact_list.write(phone + '\n')

    contact_list.close()
    print("Contact list updated!")


main()
