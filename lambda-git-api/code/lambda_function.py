import requests
import base64
import datetime

utc_now = datetime.datetime.utcnow()

# Define the time difference for IST (+5:30 hours)
ist_offset = datetime.timedelta(hours=5, minutes=30)

# Calculate the IST time by adding the offset to UTC time
ist_now = f" {utc_now + ist_offset}"



def append_file_to_repository(repo_url, file_path, pat):
    headers = {
        'Authorization': f'Token {pat}',
        'Accept': 'application/vnd.github.v3+json'
    }
    api_url = f'https://api.github.com/repos/{repo_url}/contents/{file_path + ist_now}'

    # Read the content of the file to append
    with open(file_path, 'r') as file:
        content = file.read()

    # Encode the content as base64
    encoded_content = base64.b64encode(content.encode()).decode()

    # Create the API payload
    payload = {
        'path': file_path,
        'message': 'Added new file',
        'content': encoded_content
    }

    # Send the API request to append the file
    response = requests.put(api_url, headers=headers, json=payload)
    if response.status_code == 201:
        print('File appended successfully.')
    else:
        print('Failed to append file.')


def lambda_handler(event, context):
    repository_url = "Chaitanya-Chandra/Test"         # 'username/repository-name'
    file_path = 'code.py'
    personal_access_token = os.environ['GITHUB_TOKEN']
    append_file_to_repository(repository_url, file_path, personal_access_token)
