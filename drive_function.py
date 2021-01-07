from drive_auth import *

def drive_main():
    print("Authenticate...")
    service = drive_auth_v3(["https://www.googleapis.com/auth/drive"])
    while True:
        print("Authentication complete.")
        print("--Drive Main Menu--")
        print("1.Try")
        print("0.Return to main menu")
        menu = input("Input a number to continue : ")
        if menu.isnumeric():
            menu = int(menu)
            if menu == 1:
                get_information(service)
            elif menu == 0:
                break

def get_information(api):
    # Call the Drive v3 API
    results = api.files().list(
        pageSize=100, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    print()