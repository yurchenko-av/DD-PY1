from pprint import pprint


def numeral_system(n):
    dict_of_systems = {
        'bin': bin(n),
        'dec': n,
        'hex': hex(n),
        'oct': oct(n)
    }
    numerals = []
    numerals.append(dict_of_systems)
    pprint(numerals)


list_of_systems = [numeral_system(n) for n in range(0, 16)]
