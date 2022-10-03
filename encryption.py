symbols = "23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ!#$%&*+-=?@^_il1ILo0O"


# encryption
def encryption(password):
    result = ""
    step = 3
    for i in range(len(password)):
        symbol = password[i]
        index = (symbols.find(symbol)) + step
        if index >= len(symbols):
            index -= len(symbols)
        result += symbols[index]
    return result


# decryption
def decryption(encrypted_password):
    result = ""
    step = 3
    for i in range(len(encrypted_password)):
        symbol = encrypted_password[i]
        index = (symbols.find(symbol)) - step
        if index < 0:
            index += len(symbols)
        result += symbols[index]
    return result
