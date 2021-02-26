from drive_auth import *
from drive_function import *


# Main menu
def drive_main_menu():
    print("Authenticate...")
    service = drive_auth_v3(["https://www.googleapis.com/auth/drive"])
    print("Authentication complete.")
    while True:
        print("--Drive Main Menu--")
        print("1.Manage files and folder")
        print("100.test")
        print("0.Return to main menu")
        menu = input("Input a number to continue : ")
        if menu.isnumeric():
            menu = int(menu)
            if menu == 1:
                drive_menu1(service)
                print()
            elif menu == 100:
                get_information(service)
            elif menu == 0:
                break
            else:
                print("Invalid Input")
                print()
        else:
            print("Invalid Input")
            print()


def drive_menu1(api):
    print("1.Create folder and upload .jpg file")
    menu = input("Input a number to continue : ")
    if menu.isnumeric():
        menu = int(menu)
        if menu == 1:
            print()
            create_folder_and_upload(api)

