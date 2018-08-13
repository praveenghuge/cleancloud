import create_connection
from azure.mgmt.compute import ComputeManagementClient

# connection = create_connection.get_connection()
# print(connection)

#@create_connection.get_connection
def get_vm_list():
    credentials, subscription_id = create_connection.get_connection()
    compute_client = ComputeManagementClient(credentials, subscription_id)
    print(type(compute_client.virtual_machines.list_all()))
    vm_list = compute_client.virtual_machines.list_all()
    print(dir(vm_list))

get_vm_list()