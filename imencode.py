import cv2

im = cv2.imread('/home/rg/Downloads/image1.jpg')

res, im_jpg = cv2.imencode('.jpg', im)

with open('/home/rg/src_code/images/image1.jpg', 'wb') as f:
    f.write(im_jpg.tobytes())
