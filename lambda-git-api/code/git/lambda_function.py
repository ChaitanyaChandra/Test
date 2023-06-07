import subprocess
import os

def lambda_handler(event, context):
    personal_access_token = os.environ['GITHUB_TOKEN']
    command = f"./git_code.sh {personal_access_token}"

    # Execute the command and print the output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    
    # Return a response if needed
    return {
        'statusCode': 200,
        'body': 'GitHub commands executed successfully.'
    }
