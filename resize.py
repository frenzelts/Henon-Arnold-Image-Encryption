import numpy as np
import cv2

def resize(image_matrix, image_size):
    [height, width, dimension] = image_size
    
    new_size = max(height, width)
    
    resized_img = np.zeros((new_size,new_size,3), np.uint8)
    resized_img[:,:] = (255,255,255)
    
    x_offset = np.uint8((new_size-width)/2)
    y_offset = np.uint8((new_size-height)/2)

    resized_img[y_offset:y_offset+height, x_offset:x_offset+width] = image_matrix.copy()

    return resized_img 