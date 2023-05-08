import boto3
import csv
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
        instance_data.append({"InstanceId" : instance['InstanceId'], "Service" : tag_dict.get('Service'), "Name" : tag_dict.get('Name'), "Environment" : tag_dict.get('Environment'), "instanceType" : instance['InstanceType']})
        # print(instance) 'Tags': [{'Key': 'user', 'Value': 'chaitanya'}]  list(dict)


# print(instance_data)

metrics = [{'CPUUtilization' : 'Percent'},{'NetworkInBytes':'Bytes'} , {'NetworkOutBytes' : 'Bytes'}]

def calculate(days):
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days)

    for metric in metrics:
        for k, v in metric.items():
            for data in instance_data:
                response = cloudwatch.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName=k,
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
                    Unit=v
                )

                datapoints = response['Datapoints']
                print(datapoints)
                metric_datapoints = []
                if len(datapoints) > 0:
                    for datapoint in datapoints:
                        metric_datapoints.append(datapoint.get('Average'))
                    # print(average_cpu)
                    average_metric = sum(metric_datapoints) / len(metric_datapoints)
                    data.update({f"Average_{k}_past_{days}_days" : average_metric})
                    # print(f"{data.get('InstanceId')} Average CPU utilization over the past {days} days: {average_cpu:.2f}%")
                else:
                    print(f"No data available for the past {days} days.")


calculate(5)
calculate(10)
calculate(15)
keys = instance_data[0].keys()
# Write the instance data to a CSV file
with open('instance_data.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(instance_data)

# print(instance_data)