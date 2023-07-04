import boto3
import pandas as pd

file_name = 'server.csv'
ec2 = boto3.resource('ec2',region_name="us-east-1")
aws_con= boto3.session.Session()
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")


df = pd.read_csv(file_name)
for ind in df.index:
    print(f"Creating the instance {df['Name'][ind]} ")
    Name=df['Name'][ind]
    instances = ec2.create_instances(
        ImageId=df['ami_id'][ind],
        MinCount=int(df['min_count'][ind]),
        MaxCount=int(df['max_count'][ind]),
        InstanceType=df['instance_type'][ind],
        KeyName=df['key_name'][ind],
        TagSpecifications=[
        {   'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': Name
                },
            ]
        },
    ],
    )
    print(f"Waiting for instance {df['Name'][ind]} to get started")
    waiter = ec2_con_cli.get_waiter('instance_running')
    waiter.wait(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [Name]
        },
        
        
    ],
    )
    print(f"EC2 instance {df['Name'][ind]} started successfully")
    
    