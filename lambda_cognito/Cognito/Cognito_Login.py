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

        response = cognito.initiate_auth(
            Client_id=client_id,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME':username,
                'PASSWORD':password
            }
        )

        if response['AuthenticationResult']:
            access_token = response['AuthenticationResult']['AccessToken']
            id_token = response['AuthenticationResult']['IdToken']
            refresh_token = response["AuthencationResult"]['RefreshToken']
            
            print(response)

            return {
                'statusCode':200,
                'body': 'Login Successful SSIBAL!!! :)',
                'access_token':access_token,
                'id_token':id_token,
                'refresh_token':refresh_token
            }
        else :
            return {
                'statusCode':401,
                'body': 'Invalid credentials SSIBAL... :('
            }            
       
    
    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'body': 'Error during login SSIBAL... :('
        }