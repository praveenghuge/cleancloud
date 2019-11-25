from azure.common.credentials import ServicePrincipalCredentials

tenant_id = ""
client_secret = ""
subscriptionid = ""
client_id = ""

def get_connection():
    subscription_id = subscriptionid
    credentials = ServicePrincipalCredentials(client_id=client_id,secret=client_secret,tenant=tenant_id)
    return  credentials,subscription_id



