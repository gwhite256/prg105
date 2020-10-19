class Personal:

    def __init__(self, name_in, address_in, age_in, phone_in):
        self.__name = name_in
        self.__address = address_in
        self.__age = age_in
        self.__phone = phone_in

    def set_name(self, name_in):
        self.__name = name_in

    def set_address(self, address_in):
        self.__address = address_in

    def set_age(self, age_in):
        self.__age = age_in

    def set_phone(self, phone_in):
        self.__phone = phone_in

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def __str__(self):
        return "Name: " + self.__name + "\nAddress: " + self.__address +\
            "\nAge: " + self.__age + "\nPhone Number: " + self.__phone


def main():
    person1 = Personal("Garrett", "7911 Pinoak Dr.", "21", "815-363-1975")
    person2 = Personal("Bill", "123 Happy St.", "32", "815-234-6743")
    person3 = Personal("Sam", "1860 N Richmond Rd.", "38", "815-385-0606")
    print(person1)
    print()
    print(person2)
    print()
    print(person3)


main()
