import random
import string


def generating(numbers):
    GeneratedPassword = ""
    for i in range(0, numbers):
        GeneratedPassword += random.choice(passwords)
    print(f"it's your password - {GeneratedPassword}")
    response = str(input(" Do you want to regenerate ? Y/N")).lower()
    if response == "y":
        generating(numbers)
    else:
        print("Thank YOU for Using me. ")


codes = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_"]
passwords = codes + symbol
y = True

while y:
    number = int(input("Enter the length of Your Password : "))
    if 1 <= number <= 4:
        choice = str(input("This will be a Week Password ! Are You Sure You want to Continue ? Y/N")).lower()
        if choice == "n":
            y = False
        else:
            generating(number)
    elif 5 <= number <= 7:
        choice = str(input("This will be a Moderate Password ! Are you sure want to continue ? Y/N")).lower()
        if choice == "n":
            y = False
        else:
            generating(number)
    elif number >= 8:
        choice = str(input("yup! it will be a Hard password ! Want to continue ? Y/N")).lower()
        if choice == "n":
            y = False
        else:
            generating(number)
