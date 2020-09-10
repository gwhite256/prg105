def main():
    print("This program will tell you more about a videogame character of your choice")
    print("A. Master Chief")
    print("B. Jesse Faden")
    print("C. Cal Kestis")
    print("D. Corvo Attano")
    print("E. Gordon Freeman")
    print("")
    choice = input("Enter a letter: ")

    if choice == "A" or choice == "a":
        a()
    elif choice == "B" or choice == "b":
        b()
    elif choice == "C" or choice == "c":
        c()
    elif choice == "D" or choice == "d":
        d()
    elif choice == "E" or choice == "e":
        e()
    else:
        print("You didnt enter a valid letter")


def a():
    print("Master Chief is a spartan 2 super soldier with call sign sierra 117.")
    print("He saved humanity from the overwhelming alien force of the Covenant")
    print("")


def b():
    print("Jesse Faden has mysterious powers that she will need in order to")
    print("traverse the Federal Bureau of Control and defeat the Hiss ")
    print("")


def c():
    print("Cal Kestis, a jedi padawan who was going to finish jedi training before order 66 occurred.")
    print("Fights back against the empire in the early stages of the rebellion")
    print("")


def d():
    print("Corvo Attano was the Former royal protector who was betrayed by corrupt politicians")
    print("by blaming him for the murder of queen Jessamine Kaldwin.")
    print("Helps topple the new government and rescues the queen’s daughter Emily.")
    print("")


def e():
    print("Gordon Freeman is a theoretical physicist who is thrown into an unusual situation")
    print("as the Black Mesa testing facility is getting overrun by interdimensional aliens")
    print("called the Combine. Goes on to fight the Combine in the next few games")
    print("")


main()
