words = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
num = input("Enter a number: ")
for digit in num:
    print(words[int(digit)], end=" ")