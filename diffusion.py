import numpy as np
import os
import cv2
import time

def pixelManipulation(image):
    print("Begin diffusion...")
    [row, col, dim] = image.dimension

    alpha = image.matrix[:,:,3]

    #Generate Henon map using the image dimension
    start_time = time.perf_counter()
    henon_map = generateHenonMap(image)
    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:0.4f} seconds")
    
    start_time = time.perf_counter()
    resultant_matrix = []
    image_matrix_rgb = []
    
    #Flatten the henon map and image matrix per channel
    henon_map_flatten = henon_map.flatten()
    for i in range(3):
        image_matrix_rgb.append(image.matrix[:,:,i].flatten())
    
    #Perform the XOR operation between the Henon Map and Image Matrix for each channel
    for i in range(3):
        resultant_matrix.append(np.bitwise_xor(henon_map_flatten, image_matrix_rgb[i])) 
    resultant_matrix = np.asarray(resultant_matrix)

    #Reconstruct the image matrix to its original shape
    resultant_matrix_b = np.reshape(resultant_matrix[0], [row,col])
    resultant_matrix_g = np.reshape(resultant_matrix[1], [row,col])
    resultant_matrix_r = np.reshape(resultant_matrix[2], [row,col])
    resultant_matrix = np.dstack((resultant_matrix_b, resultant_matrix_g, resultant_matrix_r, alpha))
    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    return resultant_matrix

def generateHenonMap(image):
    x = image.key.henon.x
    y = image.key.henon.y
    [row, col, dim] = image.dimension
    sequence_size = row * col * 8
    bit_sequence = [] #array contains 8 bits
    byte_array = []
    for i in range(sequence_size):
        #Henon map formula
        xN = y + 1 - 1.4 * x**2
        yN = 0.3 * x
        
        #xN and yN becomes the new x and y
        x = xN
        y = yN

        #Convert to binary using the threshold value
        if xN <= 0.3992:
            bit = 0
        else:
            bit = 1
        #insert bit to bit_sequence
        try:
            # bit_sequence = np.append(bit_sequence, bit)
            bit_sequence.append(bit)
        except:
            bit_sequence = [bit]
        # convert to decimal
        if i % 8 == 7:
            decimal = dec(bit_sequence)
            try:
                # byte_array = np.append(byte_array, decimal)
                byte_array.append(decimal)
            except:
                byte_array = [decimal]
            bit_sequence = []
    byte_array = np.asarray(byte_array)
    henon_map = np.reshape(byte_array, [row, col])
    return henon_map

def dec(bitSequence):
    decimal = 0
    for bit in bitSequence:
        decimal = decimal * 2 + int(bit)
    return decimal