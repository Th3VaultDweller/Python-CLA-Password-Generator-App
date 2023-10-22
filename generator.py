import datetime
import random
import string
from os.path import exists, isfile

path = "generated_passwords.txt"


def password(random_symbols):
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
    random_symbols = (
        random.choices(letters_list, k=5)
        + random.choices(symbols_list, k=3)
        + random.choices(numbers_list, k=2)
        + random.choices(symbols_list, k=3)
    )
    return random_symbols


generated_password = str(password(1))[:200]
today = datetime.datetime.today()
if path:
    f = open("generated_passwords.txt", "a")
    f.write(
        f"{today:%B %d, %Y}\n Here's your another password: \r\n {generated_password} \r\n"
    )
    f.close
else:
    f = open("generated_passwords.txt", "w+")
    f.write(f"{today:%B %d, %Y}\n Here's your password: \r\n {generated_password} \r\n")
    f.close


print(f"Here's your password: {generated_password}")

input("Run the app again to generate a new one? y/N")
if input == "y":
    # print(f"Here's another password: {generated_password}")
    f = open("generated_passwords.txt", "a")
    f.write(
        f"{today:%B %d, %Y}\n Here's your password: \r\n {(str(password(1))[:200])} \r\n"
    )
    f.close
