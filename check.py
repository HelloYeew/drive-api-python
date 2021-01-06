import subprocess
import sys
import urllib.request
import os

def check_library():
    print("Start checking important library to run a program...")

    # check google api python client
    print("Checking Google API Python Client...")
    try:
        import googleapiclient
    except ImportError:
        print("Google API Python Client not found.")
        print("Run install command : pip install --upgrade google-api-python-client")
        subprocess.check_call([sys.executable, "-m", "pip", "install", '--upgrade', 'google-api-python-client'])
        print("Google API Python Client install complete!")
    finally:
        import googleapiclient

    # check google oauth
    print("Checking Google Oauth Library...")
    try:
        import google_auth_oauthlib
    except ImportError:
        print("Google Oauth Library not found.")
        print("Run install command : pip install --upgrade google-auth-oauthlib google-auth-httplib2")
        subprocess.check_call([sys.executable, "-m", "pip", "install", '--upgrade', 'google-auth-oauthlib', 'google-auth-httplib2'])
        print("Google Oauth Library Client install complete!")
    finally:
        import google_auth_oauthlib

    # check oauth2client
    print("Checking oauth2client...")
    try:
        import oauth2client
    except ImportError:
        print("oauth2client not found.")
        print("Run install command : pip install --upgrade google-auth-oauthlib google-auth-httplib2")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", '--upgrade', 'oauth2client'])
        print("oauth2client install complete!")
    finally:
        import oauth2client

    print("Checking complete!")


def check_internet(url='http://www.google.com', timeout=3):
    try:
        urllib.request.urlopen(url, timeout=timeout)
        return True
    except Exception as e:
        print(e)
        return False


def check_token():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.pickle'):
                return True
