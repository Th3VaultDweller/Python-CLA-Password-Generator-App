import datetime
import random
import secrets
import string
from os.path import exists, isfile

path = "generated_passwords.txt"


def get_password(random_symbols):
    random_symbols = list(
        secrets.choice(string.hexdigits)
        + secrets.choice(string.punctuation)
        + secrets.choice(string.hexdigits)
        + secrets.choice(string.hexdigits)
        + secrets.choice(string.punctuation)
        + secrets.choice(string.hexdigits)
        + secrets.choice(string.hexdigits)
        + secrets.choice(string.punctuation)
        + secrets.choice(string.hexdigits)
    )
    return random_symbols


def user_input(self):
    input("Run the app again to generate a new one? Y/N\n")


def write_password_to_file(self):
    if path:
        # если файл существует, в него прикрепляется сгенерированный пароль
        f = open("generated_passwords.txt", "a")
        f.write(
            f"{today:%B %d, %Y}\n Here's your password: {password_no_brackets} \r\n"
        )
        f.close
    else:
        # если файла не существует, он создаётся, и в него записывается пароль
        print(f"Here's your password: {(password_no_brackets)}")
        f = open("generated_passwords.txt", "w+")
        f.write(
            f"{today:%B %d, %Y}\n Here's your password: {password_no_brackets} \r\n"
        )
        f.close


generated_password = (get_password(1))[:200]  # есть скобки, пробелы и запятые
password_no_brackets = "".join(generated_password)
today = datetime.datetime.today()  # дата создания пароля

while True:
    if user_input(1) == "Y" or "y":
        print(f"Here's your password: {(password_no_brackets)}")
        # вывод и запись одного и того же пароля в терминал и в файл
        write_password_to_file(1)
        print(f"Here's your another password: {(password_no_brackets)}")

    if user_input == "N" or "n":
        print("Closing the app. See you soon.")
        break

    # user_input(1)
