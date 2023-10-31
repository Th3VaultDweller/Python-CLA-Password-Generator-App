import datetime
import random
import string
from os.path import exists, isfile

path = "generated_passwords.txt"


def get_password(random_symbols):
    random_symbols = list(
        random.choices(string.hexdigits, k=5)
        + random.choices(string.punctuation, k=3)
        + random.choices(string.hexdigits, k=5)
    )
    return random_symbols


def user_input(self):
    input("Run the app again to generate a new one? Y/N\n")


def write_password(self):
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
    print(f"Here's your password: {(password_no_brackets)}")
    user_input(1)
    if path:
        write_password(1)

    if user_input == "N" or "n":
        print("Closing the app. See you soon")
        break
