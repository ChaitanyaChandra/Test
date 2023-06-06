import urllib3
import base64
import datetime
import os
import json

utc_now = datetime.datetime.utcnow()

# Define the time difference for IST (+5:30 hours)
ist_offset = datetime.timedelta(hours=5, minutes=30)

# Calculate the IST time by adding the offset to UTC time
ist_now = utc_now + ist_offset


def append_file_to_repository(repo_url, file_path, file_name, pat):
    http = urllib3.PoolManager()

    headers = {
        'Authorization': f'Token {pat}',
        'Accept': 'application/vnd.github.v3+json'
    }
    api_url = f'https://api.github.com/repos/{repo_url}/contents/{ist_now.strftime("%Y/%m/") + file_name + ist_now.strftime(" %dth %A at %H:%M:%S")}'

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

    # Convert payload to bytes
    payload_bytes = json.dumps(payload).encode('utf-8')

    # Send the API request to append the file
    response = http.request('PUT', api_url, headers=headers, body=payload_bytes)

    if response.status == 201:
        print('File appended successfully.')
    else:
        print('Failed to append file.')


def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            # Perform any necessary operations with the file
            # For example, write some content to the file
            file.write(f'This is some xml content {ist_now}')

        print(f'File created successfully: {file_path}')
    except IOError as e:
        print(f'Error creating file: {str(e)}')


def lambda_handler(event, context):
    repository_url = "Chaitanya-Chandra/Test"  # 'username/repository-name'
    file_path = '/tmp/code.xml'
    file_name = 'code.xml'
    personal_access_token = os.environ['GITHUB_TOKEN']
    create_file(file_path)
    append_file_to_repository(repository_url, file_path, file_name, personal_access_token)
