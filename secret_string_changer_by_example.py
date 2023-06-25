import random
import string

secret_string = "INSERT YOUR SECRET STRING"

example_output = ""
for i in secret_string:
    if i.isdigit():
        i = random.randint(0, 9)
        example_output += str(i)
    elif i.isalpha():
        i = random.choice(string.ascii_letters)
        example_output += i
    else:
        example_output += i
print(example_output)
