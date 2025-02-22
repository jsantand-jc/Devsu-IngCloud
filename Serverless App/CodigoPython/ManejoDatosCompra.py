import json
import boto3
import uuid
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Fetch the region from environment variable or use a default
region = os.environ.get('Region', 'us-east-1')

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name=region)

# Specify the table
table = dynamodb.Table('ComprasProductos')

def lambda_handler(event, context):
    logger.info('Received event: %s', json.dumps(event, indent=2))

    for record in event['Records']:
        body = record['body']
        logger.info('Record body: %s', body)
        
        # Parse the body as JSON
        body = json.loads(body)
        
        try:
            # Extract fields
            IdProducto = body.get('IdProducto')
            NombreProducto = body.get('NombreProducto')
            Categoria = body.get('Categoria')
            PrecioPorUnidad = body.get('PrecioPorUnidad')
            IdCliente = body.get('IdCliente')
            NombreCliente = body.get('NombreCliente')
            HoradeCompra = body.get('HoraDeCompra')

            # Check for missing fields
            if not all([IdProducto, NombreProducto, Categoria, PrecioPorUnidad, IdCliente, NombreCliente, HoradeCompra]):
                logger.warning('Missing one or more fields in the message.')
                continue

            # Generate a unique key for the entire product purchase entry
            ProductPurchaseKey = str(uuid.uuid4())

            # Insert a single item with all attributes
            table.put_item(Item={
                'ProductPurchaseKey': ProductPurchaseKey,
                'IdProducto': IdProducto,
                'NombreProducto': NombreProducto,
                'Categoria': Categoria,
                'PrecioPorUnidad': PrecioPorUnidad,
                'IdCliente': IdCliente,
                'NombreCliente': NombreCliente,
                'HoradeCompra': HoradeCompra
            })

            logger.info('Item insertado con éxito en BD')

        except Exception as e:
            logger.error('Error occurred: %s', str(e), exc_info=True)

    return {}
