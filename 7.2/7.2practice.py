

def main():

    code = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '010', '011',
            '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022',
            '023', '024', '025', '026', '027', '028', '029', '031']

    standard = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z', ' ', ',', '.', '?', '!']

    phrase = input('Enter a phrase to be converted into a secret code: ')

    code_final = ""
    for letter in phrase:
        for item in range(0, len(standard)):
            if letter.upper() == standard[item]:
                code_final += (code[item] + " ")

    print("The secret code is: " + code_final)

    outfile = open("secret_code.txt", 'w')
    for letter in code_final:
        outfile.writelines(letter)
    outfile.close()
    print("Secret code has been saved")

main()
