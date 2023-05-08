import boto3
from datetime import datetime, timedelta
ec2 = boto3.client('ec2')

# Set up the tag key and value to search for
tag_key = 'Service'
tag_value = 'stimulator_service'

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
instance_ids = ()
instance_name = ()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])
        print(instance)


# Print the instance IDs
print(instance_ids)