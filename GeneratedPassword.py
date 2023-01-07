import random
import string


def check_choice(choice, length):
    if choice == 1:
        character = string.digits
        password = random.sample(character, length)
        password = "".join(password)
    elif choice == 2:
        character = string.ascii_letters
        password = random.sample(character, length)
        password = "".join(password)
    elif choice == 3:
        character = string.digits + string.ascii_letters
        password = random.sample(character, length)
        password = "".join(password)
    elif choice == 4:
        character = string.digits + string.ascii_letters + string.punctuation
        password = random.sample(character, length)
        password = "".join(password)
    else:
        print("Wrong Choice")
        password = None
    return password


def main():
    length = int(input("Please Enter length: "))
    choice = int(input("Please Enter choice"
                       "\n1: Digit only"
                       "\n2: Letter only"
                       "\n3: Digit + Letter"
                       "\n4: Digit + Letter + Punctuation"
                       "\nEnter:"))
    password = check_choice(choice, length)
    print("The generated password =", password)

main()