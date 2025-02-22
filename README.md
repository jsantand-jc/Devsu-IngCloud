# Repositorio del Reto Técnico Ingeniero Cloud

- Se incluye el documento explicativo a las consultas teoricas
- Diagrama de Arquitectura del Caso Practico
- Recursos para construir el caso Practico sobre AWS

## Requisitos:
1. Cuenta AWS: Free Tier Account
2. AWS CLI
3. Visual Studio Code

## Recursos:

* Politicas de seguridad para S3
* Coidgo Python Ejemplo para funciones Lambda
* Codigo para formulario Web

## Servicios AWS:
* Amazon S3
* Amazon Lambda
* Amazon SQS
* Amazon API Gateway
* Amazon DynamoDB

## Tareas de Configuración:

1. Creación de una tabla en DynamoDB con una Partition Key, Configuraciones por Defecto
2. Creación de una Cola estandard en Amazon SQS
3. Configuración de Funcion Lambda que se dispara el momento que se reciben mensajes en la cola y almacena los items en la tabla de DynamoDB
4. Configurar los permisos necesarioes en Lambda para permitir accesos a Log y tareas de inserción en DynamoDB. Adicional los permisos para escribir en Cloudwatch.
5. Creación de una Rest API en API Gateway que sea llamada desde el formato HTML con un método PUT integrado a Lambda.
6. Creación de la función lambda a ser invocada desde la API y que llevará el mensaje hasta la cola en Amazon SQS.
7. Configuración de los permisos necesarios en lambada para SQS y Cloudwatch.
8. Creacion del Bucket en S3 configurado como Static Website y configurar las politicas de acceso público.
   
