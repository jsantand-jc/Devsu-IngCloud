import json
import boto3
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the SQS client
sqs = boto3.client('sqs', region_name=os.environ['AWS_REGION'])

def lambda_handler(event, context):
    logger.info('Received event: %s', event)

    try:
        # Extract the body from the event
        body = event['body']
        logger.info('Message body: %s', body)

        # Set up SQS parameters
        params = {
            'MessageBody': body,
            'QueueUrl': 'https://sqs.us-east-1.amazonaws.com/381492201178/ProductPurchasesDataQueue'
        }

        # Send the message to the SQS queue
        response = sqs.send_message(**params)
        logger.info('Message sent to SQS with MessageId: %s', response['MessageId'])

        # Return a successful response
        return {
            'statusCode': 200,
            'headers': { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' },
            'body': json.dumps({'status': 'success', 'messageId': response['MessageId']})
        }

    except Exception as e:
        logger.error('Error sending message to SQS: %s', str(e), exc_info=True)
        
        # Return an error response
        return {
            'statusCode': 500,
            'headers': { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' },
            'body': json.dumps({'status': 'error', 'message': str(e)})
        }
