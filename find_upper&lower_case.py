text = input("Enter a string: ")
ucc = 0
lcc = 0
for char in text:
    if char.isupper():
        ucc += 1
    elif char.islower():
        lcc += 1
print(f"Number of upper case letters: {ucc}")
print(f"Number of lower case letters: {lcc}")