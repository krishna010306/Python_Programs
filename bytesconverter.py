a = int(input("Enter the bits="))
bytes = 8
kilobyte = 1024
megabyte = 1024
gigabyte = 1024
terabyte = 1024

in_bytes = a / bytes
print("In bytes:",in_bytes)

in_kilobyte = in_bytes / kilobyte
print("In kilobyte:",in_kilobyte)

in_megabyte = in_kilobyte / megabyte
print("In megabyte:",in_megabyte)

in_gigabyte = in_megabyte / gigabyte
print("In gigabyte:",in_gigabyte)

in_terabyte = in_gigabyte / terabyte
print("In terabyte:",in_terabyte)