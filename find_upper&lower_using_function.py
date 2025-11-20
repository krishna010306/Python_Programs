def cal(text):
    up = 0
    lc = 0
    for char in text:
        if char.isupper():
            up += 1
        elif char.islower():
            lc += 1
    return up, lc
text = input("Enter a string: ")
up, lc = cal(text)
print(f"Number of upper case letters: {up}")
print(f"Number of lower case letters: {lc}")