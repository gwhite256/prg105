

def main():
    numbers = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'quatro', 'five': 'cinco', 'six': 'seis',
               'seven': 'siete', 'eight': 'ocho', 'nine': 'nueve', 'ten': 'diez'}
    for value in numbers:
        answer = input("How do you say " + value + ' in spanish: ')
        print(answer)
