import boto3
from datetime import datetime, timedelta
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')


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
        instance_data.append({"InstanceId" : instance['InstanceId'], "Service" : tag_dict.get('Service'), "Name" : tag_dict.get('Name'), "Environment" : tag_dict.get('Environment')})
        # print(instance) 'Tags': [{'Key': 'user', 'Value': 'chaitanya'}]  list(dict)


# Print the instance IDs
# print(instance_data)


end_time = datetime.utcnow()
start_time = end_time - timedelta(days=30)
for data in instance_data:


    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': data.get('InstanceId')
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=3600,
        Statistics=['Average'],
        Unit='Percent'
    )

    # Print the average CPU utilization metric for the past 30 days
    datapoints = response['Datapoints']
    if len(datapoints) > 0:
        average_cpu = datapoints[-1]['Average']
        print(f"{data.get('InstanceId')} Average CPU utilization over the past 30 days: {average_cpu:.2f}%")
    else:
        print("No data available for the past 30 days.")
