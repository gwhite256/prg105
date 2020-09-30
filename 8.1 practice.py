

def main():
    words = input("Enter a series of words that you wish to turn into an acronym: ")
    split = words.split()
    acronym = ""
    for word in split:
        acronym += word[0]
    acronym = acronym.upper()
    print(acronym)


main()
