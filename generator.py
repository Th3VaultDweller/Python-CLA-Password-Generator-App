import random
import string

letters_list = [
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
]
numbers_list = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]
symbols_list = [
    "~",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "+",
    "=",
    "|",
    "/",
    "?",
    ".",
]


def password(random_symbols):
    random_symbols = (
        random.choice(letters_list)
        + random.choice(numbers_list)
        + random.choice(symbols_list)
        + random.choice(numbers_list)
        + random.choice(symbols_list)
        + random.choice(letters_list)
        + random.choice(letters_list)
        + random.choice(symbols_list)
        + random.choice(letters_list)
        + random.choice(letters_list)
        + random.choice(symbols_list)
        + random.choice(numbers_list)
        + random.choice(symbols_list)
    )
    return random_symbols


generated_password = str(password(1))[:25]


f = open("generated_passwords.txt", "w+")
f.write(f"This is your generated password: {(str(password(1))[:25])}")
f.close


print(f"Here's your password: {generated_password}")
print("Run the app again to generate a new one.")
