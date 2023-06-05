import boto3
import os

def lambda_handler(event, context):
    # AWS SDK Configure
    region = os.environ['REGION']
    client_id = os.environ['CLIENT_ID']
    user_pool_id = os.environ['USER_POOL_ID']
    cognito = boto3.client('cognito-idp', region_name = region)

    try:
        # User Information Delete request
        username = event['username']

        response = cognito.admin_delete_user(
            UserPoolId=user_pool_id,
            Username=username
        )

        # if Delete Request is Success return Successful Code
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {
                'statusCode': 200,
                'body': 'User information deleted successfully!! SSIBAL!!'
            }
        else:
            return {
                'statusCode': 400,
                'body': 'Error deleting user information... SSIBAL...'
            }
    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'body': 'Error during user information deletion... SSIBAL...'
        }
