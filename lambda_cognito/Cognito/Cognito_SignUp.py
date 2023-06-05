import boto3
import os

def lambda_handler(event, context):
    # AWS SDK Configure
    region = os.environ['REGION']
    client_id = os.environ['CLIENT_ID']
    user_pool_id = os.environ['USER_POOL_ID']
    cognito = boto3.client('cognito-idp', region_name = region)

    try:
        # User Register Request
        username = event['user_name']
        password = event['user_password']
        name = event['name'] 
        email = event['email']

        response = cognito.sign_up(
            ClientID = client_id,
            Username = username,
            Password = password,
            UserAttributes=[
                {'Name':'name', 'Value': name},
                {'Name':'email', 'Value': email}
            ]
        )

        print(response)
        return{
            'statusCode':200,
            'body': 'User registered successfully!! SSIBAL!! :)'
        }
    
    except Exception as e:
        print(str(e))
        return{
            'statusCode': 500,
            'body': 'Registering User ERROR... SSIBAL... :('
        }