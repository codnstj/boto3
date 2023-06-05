import os

def lambda_handler(event, context):
    # AWS SDK Configure
    region = os.environ['REGION']
    client_id = os.environ['CLIENT_ID']
    user_pool_id = os.environ['USER_POOL_ID']
    login_url = f'https://{user_pool_id}.auth.{region}.amazoncognito.com/login?response_type=code&client_id={client_id}&redirect_uri=https://hqigviudubhfbgdv7s4zgr6n6m0mfhal.lambda-url.ap-northeast-2.on.aws/'
    
    return {
        'statusCode': 200,
        'body': login_url
    }