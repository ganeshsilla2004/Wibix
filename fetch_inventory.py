import boto3
import sys

def fetch_stack_resources(stack_name):
    print(f"\nFetching resources for CloudFormation stack: {stack_name}\n")

    # Use default session (no hardcoded credentials)
    cf = boto3.client('cloudformation')
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')

    # Fetch stack resources
    resources = cf.describe_stack_resources(StackName=stack_name)
    print("CloudFormation Stack Resources:")
    for resource in resources['StackResources']:
        print(f"- {resource['ResourceType']}: {resource['PhysicalResourceId']}")
    print()

    # List EC2 Instances
    print("EC2 Instances:")
    ec2_res = ec2.describe_instances()
    for reservation in ec2_res['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            state = instance['State']['Name']
            print(f"- ID: {instance_id}, Type: {instance_type}, State: {state}")
    print()

    # List S3 Buckets
    print("S3 Buckets:")
    s3_res = s3.list_buckets()
    for bucket in s3_res['Buckets']:
        print(f"- {bucket['Name']}")
    print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_inventory.py <stack-name>")
        sys.exit(1)
    
    stack_name = sys.argv[1]
    fetch_stack_resources(stack_name)
