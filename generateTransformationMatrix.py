import numpy as np
import cv2

def generateHenonMap(image_size):
    x = 0.293201174303193
    y = 0.293201174303193
    [row, col, dim] = image_size
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

def generateArnoldMap(image):
    N = image.dimension[0]
    p = 20
    q = 10
    iter = 2
    M = np.array(([1,p],[q,p*q+1]))

    arnold_map = np.zeros([N,N,4], np.uint8)
    for i in range(iter):
        for y in range(N):
            for x in range(N):
                pixel_pos = np.array(([x],[y]))
                [x1, y1] = np.mod(np.dot(M,pixel_pos),N)
                arnold_map[x1,y1] = image.matrix[x,y]
    return arnold_map

def reconstructArnoldMap(image):
    N = image.dimension[0]
    p = 20
    q = 10
    iter = 2
    M = np.array(([1,p],[q,p*q+1]))

    arnold_map = np.zeros([N,N,4], np.uint8)
    for i in range(iter):
        for y in range(N):
            for x in range(N):
                pixel_pos = np.array(([x],[y]))
                [x1, y1] = np.mod(np.dot(M,pixel_pos),N)
                arnold_map[x,y] = image.matrix[x1,y1]
    return arnold_map

def dec(bitSequence):
    decimal = 0
    for bit in bitSequence:
        decimal = decimal * 2 + int(bit)
    return decimal