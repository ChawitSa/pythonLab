import random
import string
import tkinter as tk
import pyperclip as pc

'''
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
    while True:
            length = int(input("Please Enter length: "))
            choice = int(input("Please Enter choice"
                               "\n1: Digit only"
                               "\n2: Letter only"
                               "\n3: Digit + Letter"
                               "\n4: Digit + Letter + Punctuation"
                               "\nEnter:"))
            password = check_choice(choice, length)
            print("The generated password =", password)
            checker = input("Try again (y/n): ")
            if checker == 'n':
                break
'''
def generate():
    entry.delete(0, tk.END)
    length = lengthInput.get()
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbol = string.punctuation

    lowChoice = lower+upper
    mediumChoice = lowChoice+num
    strongChoice = mediumChoice+symbol

    password = ""
    if strengthInput.get() == 0:
        for i in range(length):
            password = password + random.choice(lowChoice)
    elif strengthInput.get() == 1:
        for i in range(length):
            password = password + random.choice(mediumChoice)
    else:
        for i in range(length):
            password = password + random.choice(strongChoice)

    entry.insert(0, password)

def copy():
    randomPassword = entry.get()
    pc.copy(randomPassword)


root = tk.Tk()
lengthInput = tk.IntVar()
strengthInput = tk.IntVar()

root.title("Random Password Generator")

lengthLabel = tk.Label(root, text = "Preferred Length").grid(row=0, column=0)
lengthChoice = tk.Spinbox(root, from_ = 4, to = 10, textvariable = lengthInput).grid(row=0, column=1)

strengthLabel = tk.Label(root, text = "Preferred Strength").grid(row = 0, column = 2)
lowStrength = tk.Radiobutton(root, text = "Low", variable = strengthInput, value = 0).grid(row=0, column=3)
mediumStrength = tk.Radiobutton(root, text = "Medium", variable = strengthInput, value = 1).grid(row=0, column=4)
strongStrength = tk.Radiobutton(root, text = "Strong", variable = strengthInput, value = 2).grid(row=0, column=5)

randomPassword = tk.Label(root, text = "Random Password").grid(row=1, column=0)
entry = tk.Entry(root)
entry.grid(row=1, column=1)

generateButton = tk.Button(root, text = "Generate", width=25, command = generate)
generateButton.grid(row=1, column=2)
copyButton = tk.Button(root, text = "Copy", width=5, command = copy)
copyButton.grid(row=1, column=3)

root.mainloop()


