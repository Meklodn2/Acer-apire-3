import random

letter = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "-", "/"]

print("Python paswd Generator")
# nr_letters = int(input("Qancha harif bolishini hohlaysiz?: "))
# nr_numbers = int(input("Qancha son bolishini hohlaysiz?: "))
# nr_symbols = int(input("Qancha belgi bolishini hohlaysiz?: "))
nr_symbols = 3
nr_numbers = 3
nr_letters = 3
# oson versiya
# paswd = ""
# for letter_num in range(1, nr_letters + 1):
#     rand_letter = random.randint(0, len(letter) - 1)
#     paswd += letter[rand_letter]

# for number_num in range(1, nr_numbers + 1):
#     rand_num = random.randint(0, len(numbers) - 1)
#     paswd += numbers[rand_num]


# for symbol_num in range(1, nr_symbols + 1):
#     rand_symbl = random.randint(0, len(symbols) - 1)
#     paswd += symbols[rand_symbl]

# print(paswd)

# qiyin versiya
pasword_list = []
for letter_run in range(1, nr_letters + 1):
    rand_num = random.randint(0, len(letter) - 1)
    pasword_list.append(letter[rand_num])

for symbol_run in range(1, nr_symbols + 1):
    rand_num = random.randint(0, len(symbols) - 1)
    pasword_list.append(symbols[rand_num])

for number_run in range(1, nr_numbers + 1):
    rand_num = random.randint(0, len(numbers) - 1)
    pasword_list.append(numbers[rand_num])

random.shuffle(pasword_list)


pasword = ""
for char in pasword_list:
    pasword += char
print(pasword)
