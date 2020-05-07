import generateTransformationMatrix as gtm
import numpy as np
import cv2

def pixelManipulation(image):
    [row, col, dim] = image.dimension

    #Generate Arnold cat map
    arnold_map = gtm.generateArnoldMap(image)
    print("Arnold map size: ", arnold_map.shape)

    return arnold_map