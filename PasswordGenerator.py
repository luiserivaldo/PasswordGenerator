""" Password Generator"""

import sys
import random
import string


def main():
    try:
        password_length = int(input("Insert the length of the password: "))
        if password_length > 0:
            password_generator(password_length)
            print(password_generator(password_length))
        else:
            print("Invalid input. Try again. \n")
            main()
    except ValueError:
        print("Invalid input. Try again. \n")
        main()


def password_generator(password_length):
    # variables for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # temporarily stores a random combination
    merge_variables = lowercase + uppercase + numbers + symbols
    password_proto = random.sample(merge_variables, password_length)

    # merges the combination into a string
    password_final = "".join(password_proto)

    return password_final


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

