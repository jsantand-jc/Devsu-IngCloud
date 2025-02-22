'use strict'
const AWS = require('aws-sdk')

AWS.config.update({ region: process.env.Region, apiVersion: '2012-08-10' })

const sqsClient = new AWS.SQS({apiVersion: '2012-11-05'})

module.exports.handler = async (event) => {
  
  console.log('Received event:', JSON.parse(event.body));
  
  try {

    var params = {
      MessageBody: event.body,

      QueueUrl: "https://sqs.us-east-1.amazonaws.com/381492201178/ProductPurchasesDataQueue"
    };

    const data = await sqsClient.sendMessage(params).promise();
    
    return {
        statusCode: 200,
        headers: { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: 'success', messageId: data.MessageId })
      }
    } catch (err) {
        console.error(err)
        return {
            statusCode: 200,
            headers: { 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json' },
            status: 'error',
            message: err
        }
    }
}