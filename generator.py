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


generated_password = (get_password(1))[:200]
password_no_brackets = "".join(generated_password)
today = datetime.datetime.today()  # дата создания пароля

print(f"Here's your password: {(password_no_brackets)}")

if path:
    # если файл существует, в него прикрепляется сгенерированный пароль
    f = open("generated_passwords.txt", "a")
    f.write(f"{today:%B %d, %Y}\n Here's your password: \r\n {password_no_brackets} \r\n")
    f.close
else:
    # если файла не существует, он создаётся, и в него записывается пароль
    f = open("generated_passwords.txt", "w+")
    f.write(f"{today:%B %d, %Y}\n Here's your password: \r\n {password_no_brackets} \r\n")
    f.close

# input("Run the app again to generate a new one? y/N")
# if input == "y":
#     # print(f"Here's another password: {generated_password}")
#     f = open("generated_passwords.txt", "a")
#     f.write(
#         f"{today:%B %d, %Y}\n Here's your password: \r\n {(str(password(1))[:200])} \r\n"
#     )
#     f.close
