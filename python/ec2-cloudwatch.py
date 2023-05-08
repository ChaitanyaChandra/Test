import boto3
from datetime import datetime, timedelta
ec2 = boto3.client('ec2')

# Set up the tag key and value to search for
tag_key = 'user'
tag_value = 'chaitanya'

# Filter the instances by the tag key and value
response = ec2.describe_instances(
    Filters=[
        {
            'Name': f'tag:{tag_key}',
            'Values': [tag_value]
        }
    ]
)

# Extract the instance IDs from the response
instance_data = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        tags = instance.get('Tags', [])
        tag_dict = {tag['Key']: tag['Value'] for tag in tags}
        instance_data.append({"ID" : instance['InstanceId'], "Service" : tag_dict.get('service')})
        print(tag_dict)
        # print(instance) 'Tags': [{'Key': 'user', 'Value': 'chaitanya'}]  list(dict)


# Print the instance IDs
print(instance_data)