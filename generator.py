import datetime
import random
import secrets
import string
from os.path import exists, isfile

path = "generated_passwords.txt"

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

password_length = 15


def get_password(password_length):
    my_password = ""
    for i in range(password_length):
        my_password += "".join(secrets.choice(alphabet))
    return my_password


def user_input(self):
    input("Run the app again to generate a new one? Press Y to do so.\n")


def write_password_to_file(self):
    if path:
        # если файл существует, в него прикрепляется сгенерированный пароль
        f = open("generated_passwords.txt", "a")
        f.write(
            f"{today:%B %d, %Y}\n Here's your password: {get_password(password_length)} \r\n"
        )
        f.close
    else:
        # если файла не существует, он создаётся, и в него записывается пароль
        print(f"Here's your password: {(get_password(password_length))}")
        f = open("generated_passwords.txt", "w+")
        f.write(
            f"{today:%B %d, %Y}\n Here's your password: {get_password(password_length)} \r\n"
        )
        f.close


today = datetime.datetime.today()  # дата создания пароля

while True:
    print(f"Here's your password: {(get_password(password_length))}")
    user_input(1) == "Y" or "y"
    # вывод и запись одного и того же пароля в терминал и в файл
    write_password_to_file(1)
    print(f"Here's your another password: {(get_password(password_length))}")

    if not user_input:
        print("Closing the app. See you soon.")
        break
