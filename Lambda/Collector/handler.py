import requests
import boto3
from datetime import datetime
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

    try:

        response = requests.get(url)
        data = response.json()

        btc_price = str(data['bitcoin']['usd'])
        eth_price = str(data['ethereum']['usd'])

        timestamp = datetime.utcnow().isoformat()

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('CryptoPriceTracker')

        def get_last_price(crypto_name):

            response = table.query(
                KeyConditionExpression=Key('crypto_name').eq(crypto_name),
                ScanIndexForward=False,
                Limit=1
            )

            items = response.get('Items')

            if items:
                return items[0].get('price_usd')
            else:
                return None

        last_btc_price = get_last_price('bitcoin')
        last_eth_price = get_last_price('ethereum')

        inserted = []

        if btc_price != last_btc_price:
            table.put_item(Item={
                'crypto_name': 'bitcoin',
                'timestamp': timestamp,
                'price_usd': btc_price
            })
            inserted.append(f"BTC={btc_price}")

        if eth_price != last_eth_price:
            table.put_item(Item={
                'crypto_name': 'ethereum',
                'timestamp': timestamp,
                'price_usd': eth_price
            })
            inserted.append(f"ETH={eth_price}")

        if inserted:
            message = f"Inserted new prices at {timestamp}: " + ", ".join(inserted)
        else:
            message = f"No price change detected at {timestamp}, no insertion done."

        return {
            'statusCode': 200,
            'body': message
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }