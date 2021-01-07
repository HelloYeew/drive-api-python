import sys
from check import *
# from for_dev import *
import getpass
import os

print("Booting program...")
print()

# check internet connection
print("Checking internet connection...")
connection = check_internet()
if connection == True:
    print("Connection complete!")
else:
    print("Connection failed! Please check your internet connection.")
    sys.exit()
print()

# check requirement
check_library()
print()
print("Checking directory...")
print(f"Current directory: {os.getcwd()}")
print()

# check login via token
# print("Checking login profile...")
# if check_token():
#     print("Token Available. Proceed to login")
# else:
#     print("No token available")

# menu function
from function import *
from all_apps import *
from drive_function import *
from drive_auth import *

# turn on and turn off dev mode here
dev = True

# Main Menu
while True:
    all_apps()
    num = input("Put a number to access (Exit press 0) : ")
    if num.isnumeric:
        num = int(num)
        print()
        if num == 1:
            drive_main()
        if num == 0:
            break
    else:
        print("Invalid input!")



