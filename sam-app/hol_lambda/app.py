import json
import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
client = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    print(event)
    response = client.put_item(
        Item={
            'sub_metering_1': {
                'N': str(event['sub_metering_1']),
            },
            'sub_metering_2': {
                'N': str(event['sub_metering_2']),
            },
            'sub_metering_3': {
                'N': str(event['sub_metering_3']),
            },
            'global_active_power': {
                'N': str(event['global_active_power']),
            },
            'global_reactive_power': {
                'N': str(event['global_reactive_power']),
            },
            'voltage': {
                'N': str(event['voltage']),
            },
            'timestamp': {
                'S': event['timestamp'],
            },
            'device_id': {
                'S': event['device_id'],
            },
        },
        ReturnConsumedCapacity='TOTAL',
        TableName='hol-ddb',
    )
    
    print(response)