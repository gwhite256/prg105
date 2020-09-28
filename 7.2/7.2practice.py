

def main():

    standard = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f',
                'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm',
                'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
                'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', ' ', ',', '.', '?', '!']

    code = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '010', '011',
            '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022',
            '023', '024', '025', '026', '027', '028', '029', '031', '032', '033', '034',
            '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045',
            '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057']

    outline = []

    phrase = input('Enter a phrase to be converted into a secret code: ')

    for letter in phrase:
        letter_index = standard.index(letter)
        code_value = code[letter_index]
        outline.append(code_value)

    print(outline)

    outfile = open("secret_code.txt", 'w')
    for item in outline:
        outfile.write(str(item) + "\n")
    outfile.close()


main()
