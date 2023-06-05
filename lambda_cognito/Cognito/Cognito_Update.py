import boto3
import os

def lambda_handler(event, context):
    # AWS SDK Configure
    region = os.environ['REGION']
    client_id = os.environ['CLIENT_ID']
    user_pool_id = os.environ['USER_POOL_ID']
    cognito = boto3.client('cognito-idp', region_name = region)

    try:
        # Update User Information Request
        access_token = event['access_token']
        name = event['name']
        email = event['email']

        response = cognito.update_user_attributes(
            UserAttributes=[
                {'Name': 'name', 'Value': name},
                {'Name': 'email', 'Value': email}
            ],
            AccessToken=access_token
        )

        # if Updation Request is Success Return Successful Code
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {
                'statusCode': 200,
                'body': 'User information updated successfully!! SSIBAL!! :)'
            }
        else:
            return {
                'statusCode': 400,
                'body': 'Error updating user information.. SSIBAL... :('
            }
    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'body': 'Error during user information update... SSIBAL... :('
        }
