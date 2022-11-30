import random

def get_unique_list_numbers(a, b):
    list_unique_numbers = []
    for i in range(0, 15):
        list_unique_numbers.append(random.randint(a, b))
    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers(-10, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
