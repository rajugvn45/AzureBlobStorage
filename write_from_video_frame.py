import cv2

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

connect_str = ""
container_name = ""

local_file_name = "image2.jpg"

video = cv2.VideoCapture("sBehindtheFence.avi")

retCode, frame = video.read()

if retCode:
    res, im_jpg = cv2.imencode('.jpg', frame)

    try:
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        
        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        
        #Upload to blob storage
        blob_client.upload_blob(im_jpg.tobytes())

    except Exception as ex:
        print('Exception: ', ex)


video.release()
