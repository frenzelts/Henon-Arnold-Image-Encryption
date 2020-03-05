import generateTransformationMatrix as gtm
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2

def pixelManipulation(image_matrix, image_size):
    [row, col, dim] = image_size
    print("Image size:",image_size)

    #Generate Henon map using the image dimension
    henon_map = gtm.generateHenonMap(image_size)
    print("Henon map size: ", henon_map.shape)
    
    resultant_matrix = []
    image_matrix_rgb = []
    
    #Flatten the henon map and image matrix per channel
    henon_map_flatten = henon_map.flatten()
    for i in range(3):
        image_matrix_rgb.append(image_matrix[:,:,i].flatten())
    
    #Perform the XOR operation between the Henon Map and Image Matrix for each channel
    for i in range(3):
        resultant_matrix_per_channel = []
        for j in range(henon_map_flatten.size):
            resultant_matrix_per_channel.append(henon_map_flatten[j] ^ image_matrix_rgb[i][j])
        resultant_matrix.append(resultant_matrix_per_channel) 
    resultant_matrix = np.asarray(resultant_matrix)

    #Reconstruct the image matrix to its original shape
    resultant_matrix_b = np.reshape(resultant_matrix[0], [row,col])
    resultant_matrix_g = np.reshape(resultant_matrix[1], [row,col])
    resultant_matrix_r = np.reshape(resultant_matrix[2], [row,col])
    resultant_matrix = np.dstack((resultant_matrix_b, resultant_matrix_g, resultant_matrix_r))

    return resultant_matrix