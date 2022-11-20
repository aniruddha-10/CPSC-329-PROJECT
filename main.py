from hashing import PasswordManager as pm

specialCharacters = [
    "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", ",", ":",";",
    '"', "'", "<", ">", ".", "?", "/"]


def createPassword():
    password = input(
        "Please enter a password to continue.\n Password must:\n - Be at least 8 characters in length\n - Contain a capital letter\n - Contain a lower case letter\n - Contain a number\n - Contain a special character (~, `, !, @, #, $, %, ^, &, *, (, ), _, -, +, =, {, [, }, ], |, :, ;, " + '", ' + "', <, ,, >, ., ?, /)\nPassword: ")
    password_2 = input("Please confirm password: ")
    if password != password_2:
        print("Passwords do not match, please try again.")
        createPassword()
    else:
        return password


def isValid(password):
    passCheck = 0
    bool(passCheck)
    upperCheck = 0
    bool(upperCheck)
    lowerCheck = 0
    bool(lowerCheck)
    numbCheck = 0
    bool(numbCheck)
    symbCheck = 0
    bool(symbCheck)
    lengthCheck = 0
    bool(lengthCheck)
    if len(password) >= 8:
        lengthCheck = 1
    for i in range(len(password)):
        if password[i].isupper():
            upperCheck = 1
        elif password[i].islower():
            lowerCheck = 1
        elif password[i].isdigit():
            numbCheck = 1
        elif password[i] in specialCharacters:
            symbCheck = 1
        else:
            print("Invalid character(s). Please try again.")
            createPassword()

    if not lengthCheck or not upperCheck or not lowerCheck or not numbCheck or not symbCheck:
        if not lengthCheck:
            print("This password is too short.")
        if not upperCheck:
            print("There are no upper case letters in this password.")
        if not lowerCheck:
            print("There are no lower case letters in this password.")
        if not numbCheck:
            print("There are no numbers in this password.")
        if not symbCheck:
            print("There are no special characters in this password.")
    else:
        passCheck = 1
    if not passCheck:
        print("Please try again.")
        createPassword()


def getFile():
    file_path = input("Specify filepath to save passwords: ")
    return file_path


print("Welcome!")
masterPwd = createPassword()
isValid(masterPwd)
pm.derive_master_key(pm, masterPwd)
masterPwd = ""
