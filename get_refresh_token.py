from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    flow = InstalledAppFlow.from_client_secrets_file('token.json', scopes=SCOPES)
    creds = flow.run_local_server(port=0)
    print("Refresh token:", creds.refresh_token)

if __name__ == '__main__':
    main()