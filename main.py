# import
import random
import encryption as m

# variables
digits = "23456789"
lowercase_letters = "abcdefghjkmnpqrstuvwxyz"
uppercase_letters = "ABCDEFGHJKMNPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
sus = "il1ILo0O"
symbols = ""


# functions
def open_file(var, s):
    with open("passwords.txt", "a") as f:
        f.write(var + s)


def output(line):
    x = line.split(": ")
    decryption_password = m.decryption(x[1])
    print(decryption_password)


def is_exist_password(login):
    with open("passwords.txt", "r") as f:
        lst = f.readlines()
        for line in lst:
            if login in line:
                return True, line
        else:
            return False, None


def generate_password(count_symbols, text):
    count_symbols = int(count_symbols)
    password = ""
    for o in range(count_symbols):
        password += random.choice(text)
    print(f"Ваш пароль, в файле он будет хранится в зашифрованном виде: {password}")
    encrypted_password = m.encryption(password)
    open_file(encrypted_password, "\n")


def check(symbols):
    length = input("Длина пароля?")
    need_digit = input("Нужны ли числа в пароле?")
    if need_digit.lower() == "да":
        symbols += digits
    need_punctuation = input("Нужны ли специальные символы в пароле?")
    if need_punctuation.lower() == "да":
        symbols += punctuation
    need_up = input("Добавить верхний регистр?")
    if need_up.lower() == "да":
        symbols += uppercase_letters
    need_low = input("Добавить нижний регистр?")
    if need_low.lower() == "да":
        symbols += lowercase_letters
    sus_symbols = input("Включать ли неоднозначные символы (il1LIo0O)?")
    if sus_symbols.lower() == "да":
        symbols += sus
    generate_password(length, symbols)


# inputs
login = input("Введите логин:")

# functions call
flag, line = is_exist_password(login)
if flag:
    output(line)
else:
    open_file(login, ": ")
    check(symbols)
