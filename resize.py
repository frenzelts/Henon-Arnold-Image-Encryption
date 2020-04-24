import numpy as np
import cv2

def resize(image_matrix, image_size):
    [height, width, dimension] = image_size
    
    new_size = max(height, width)
    
    resized_img = np.zeros((new_size,new_size,4), np.uint8)
    resized_img[:,:] = (255,255,255,0)
    
    x_offset = np.uint8((new_size-width)/2)
    y_offset = np.uint8((new_size-height)/2)

    image_matrix = cv2.cvtColor(image_matrix, cv2.COLOR_BGR2BGRA)

    resized_img[y_offset:y_offset+height, x_offset:x_offset+width] = image_matrix.copy()

    return resized_img 

def cropBorder(image_matrix, image_size):
    [height, width, dimension] = image_size
    img_new = np.zeros([450,600,3])
    for i in range(3):
        img_temp = image_matrix[:,:,[i,3]]
        img_temp = img_temp[img_temp[:,:,1] == 255]
        img_new[:,:,i] = np.reshape(img_temp[:,0], [int(img_temp.shape[0]/600),600])

    return img_new