import numpy as np
import cv2
import math

def squareImage(image):
    [height, width, dimension] = image.dimension
    
    new_size = max(height, width)
    
    resized_img = np.zeros((new_size,new_size,4), np.uint8)
    resized_img[:,:] = (255,255,255,254)
    
    x_offset = np.uint8((new_size-width)/2)
    y_offset = np.uint8((new_size-height)/2)

    image_matrix = cv2.cvtColor(image.matrix, cv2.COLOR_BGR2BGRA)

    resized_img[y_offset:y_offset+height, x_offset:x_offset+width] = image_matrix.copy()

    return resized_img 

def cropBorder(image):
    [height_ol, width_ol, dimension] = image.dimension
    height = (image.matrix[:,math.floor(width_ol/2),3] == 255).sum()
    print(height)
    width = (image.matrix[math.floor(height_ol/2),:,3] == 255).sum()
    print(width)
    img_new = np.zeros([height,width,3])
    for i in range(3):
        img_temp = image.matrix[:,:,[i,3]]
        img_temp = img_temp[img_temp[:,:,1] == 255]
        img_new[:,:,i] = np.reshape(img_temp[:,0], [height,width])

    return img_new