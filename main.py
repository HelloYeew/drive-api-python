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

# menu function
# from function import *

# turn on and turn off dev mode here
dev = True

# Main Menu
while True:
    print("--Main menu--")
    print(f"Hi! {getpass.getuser()}. What you want to do?")
    print("1.Fetch Video Data")
    print("2.Download Video Thumbnail")
    print("3.Download Video as mp4")
    print("0.exit")
    menu = input("Press number from menu to continue : ")