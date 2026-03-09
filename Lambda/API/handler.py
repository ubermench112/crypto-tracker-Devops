import boto3
from boto3.dynamodb.conditions import Key
import json

def lambda_handler(event, context):

    params = event.get("queryStringParameters")

    if not params:
        return {
            "statusCode": 400,
            "body": json.dumps("Missing query parameter")
        }

    crypto = params.get("crypto")

    if not crypto:
        return {
            "statusCode": 400,
            "body": json.dumps("Please provide crypto parameter")
        }

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("CryptoPriceTracker")

    response = table.query(
        KeyConditionExpression=Key("crypto_name").eq(crypto),
        ScanIndexForward=False,
        Limit=1
    )

    items = response.get("Items")

    if not items:
        return {
            "statusCode": 404,
            "body": json.dumps("Crypto not found")
        }

    return {
        "statusCode": 200,
        "body": json.dumps(items[0])
    }