import boto3
import csv
from datetime import datetime, timedelta
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')


# Set up the tag key and value to search for
tag_key = 'user'
tag_value = 'chaitanya'
days = 30

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
        instance_data.append({"InstanceId" : instance['InstanceId'], "Service" : tag_dict.get('Service'), "Name" : tag_dict.get('Name'), "Environment" : tag_dict.get('Environment'), "instanceType" : instance['InstanceType']})
        # print(instance) 'Tags': [{'Key': 'user', 'Value': 'chaitanya'}]  list(dict)


# print(instance_data)

end_time = datetime.utcnow()
start_time = end_time - timedelta(days)
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
    cpu = []
    if len(datapoints) > 0:
        for datapoint in datapoints:
             cpu.append(datapoint.get('Average'))
        # print(average_cpu)
        average_cpu = sum(cpu) / len(cpu)
        data.update({f"Average_cpu_past_{days}_days" : average_cpu})
        # print(f"{data.get('InstanceId')} Average CPU utilization over the past {days} days: {average_cpu:.2f}%")
    else:
        print(f"No data available for the past {days} days.")



# Write the instance data to a CSV file
with open('instance_data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['InstanceId', 'Service', 'Name', 'Environment', 'InstanceType', f'Average_cpu_past_{days}_days']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in instance_data:
        print(data)

print(instance_data)