import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# setx AZURE_STORAGE_CONNECTION_STRING "<yourconnectionstring>"
# Connection string is obtained from Storage account in Azure

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "imagedata"

local_file_name = "image1.png"
#local_file_name = "image2.jpg"

#upload_file_path = os.path.join(r"", local_file_name)

# Design considerations:
# Check for errors 503 and 500 and do a exponential retry. 
# In both cases, the service may return a 503 (Server Busy) or 500 (Timeout) error. 
# These errors can also occur if the service is rebalancing data partitions to allow for higher throughput. 
# The client application should typically retry the operation that causes one of these errors.

try:
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    #print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(local_file_name, "rb") as data:
        blob_client.upload_blob(data)

except Exception as ex:
    print('Exception: ')
    print(ex)