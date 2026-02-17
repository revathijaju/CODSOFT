# Simple To-Do List Program
# Created for CodSoft Python Programming Internship
# Author: Revathi R

import random
import string

length = int(input("Enter the Desired Password Length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_chars = letters + digits + symbols

password = ""
for i in range(length):
    password += random.choice(all_chars)

print("Generated Password:", password)