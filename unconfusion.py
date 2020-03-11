import generateTransformationMatrix as gtm
import numpy as np
import cv2

def pixelManipulation(image_matrix, image_size):
    [row, col, dim] = image_size
    print("Image size:",image_size)

    #Generate Arnold cat map
    arnold_map = gtm.reconstructArnoldMap(image_matrix, image_size)
    print("Arnold map size: ", arnold_map.shape)

    return arnold_map