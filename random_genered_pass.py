import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chars = ['!', '?', '*', '#']

pocet_znaku = int(input("Zadej počet znaku: "))
pocet_num = int(input("Zadej počet čísel: "))
pocet_spec = int(input("Zadej počet speciálních znaků: "))

def genered_symbols(pocet, list_symbols):
    result = ""

    for _ in range(pocet):
        ran_num = random.randint(0, len(list_symbols) - 1)
        result = result + list_symbols[ran_num]

    return result

def swap(symbols):
    symbols = list(symbols)

    for i in range(len(symbols)):
        ran_num1 = random.randint(0, len(symbols) - 1)
        ran_num2 = random.randint(0, len(symbols) - 1)

        symbols[ran_num1], symbols[ran_num2] = symbols[ran_num2], symbols[ran_num1]

    return ''.join(symbols)


password = genered_symbols(pocet_znaku, alphabet) + genered_symbols(pocet_num, numbers) + genered_symbols(pocet_spec, special_chars)
final_password = swap(password)

print(final_password)
