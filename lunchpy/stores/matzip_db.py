import time
import boto3
import lunchpy.stores.matzip as matzip

"""
table name LUNCH_PY
single table strategy
partition key: LUNCH_PY_ID
partition key pattern : MATZIP_NAME#{matzip.name}
""" 

# save matzip to PK = MATZIP_NAME#{matzip.name}
def saveMatzip(matzip):
    # get dynamodb
    dynamodb = boto3.resource('dynamodb')

    # get table
    table = dynamodb.Table('LUNCH_PY')

    # set time_to_live to epoch time from now + 7 day
    time_to_live = getTimeToLive()

    # latest_recommend_time is ISO 8601 format
    table.put_item(
        Item={
            'LUNCH_PY_ID': f'MATZIP_NAME#{matzip.name}',
            'name': matzip.name,
            'rating': matzip.rating,
            'address': matzip.address,
            'recommend_count': matzip.recommend_count,
            'latest_recommend_time': time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime()),
            'time_to_live': time_to_live
        }
    )

# load matzip from PK = MATZIP_NAME#{matzip.name}
def loadMatzip(name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('LUNCH_PY')
    response = table.get_item(
        Key={
            'LUNCH_PY_ID': f'MATZIP_NAME#{name}'
        }
    )
    item = response['Item']
    return matzip.Matzip(item['name'], item['rating'], item['address'], item['recommend_count'])

# check if matzip exists in PK = MATZIP_NAME#{matzip.name} and if it does, update it
def updateMatzip(matzip):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('LUNCH_PY')
    response = table.get_item(
        Key={
            'LUNCH_PY_ID': f'MATZIP_NAME#{matzip.name}'
        }
    )
    # if matzip exists, update with 1 more recommend_count
    # set time_to_live to 7 days
    time_to_live = getTimeToLive()
    if 'Item' in response:
        item = response['Item']
        table.update_item(
            Key={
                'LUNCH_PY_ID': f'MATZIP_NAME#{matzip.name}'
            },
            UpdateExpression="set recommend_count = recommend_count + :val, time_to_live = :ttl",
            ExpressionAttributeValues={
                ':val': 1,
                ':ttl': time_to_live
            },
            ReturnValues="UPDATED_NEW"
        )
    # if matzip does not exist, do nothing
    else:
        pass

def getTimeToLive():
    return int(time.time()) + 7 * 24 * 60 * 60