from googleapiclient.http import MediaFileUpload


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


def create_folder_and_upload(api):
    # Ask Required Information
    name = input("Folder Name : ")
    file_name = input("File name (with .jpg) :")

    # Create Folder
    file_metadata = {
        'title': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = api.files().insert(body=file_metadata, fields='id').execute()
    print('Folder ID: %s' % file.get('id'))

    # Upload Files
    folder_id = file.get('id')
    file_metadata = {
        'title': file_name,
        'parents': [{'id': folder_id}]
    }
    media = MediaFileUpload('files/photo.jpg',
                            mimetype='image/jpeg',
                            resumable=True)
    file = api.files().insert(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID: %s' % file.get('id'))