import generateTransformationMatrix as gtm
import imagePreprocessing as ip
# from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2

def pixelManipulation(image_path, image_name):
    print(image_name)
    image_matrix = ip.getImageMatrix(image_path)
    image_size = ip.getImageSize(image_matrix)
    [w, h, d] = image_size
    print("Image size:",image_size)
    henon_map = gtm.generateHenonMap(image_size)
    print("Henon map size: ", henon_map.shape)
    
    #Performing XOR Operation between the transformation Matrix and ImageMatrix
    #Storing the result in resultant Matrix
    resultant_matrix = []
    image_matrix_bgr = []
    for i in range(3):
        image_matrix_bgr.append(image_matrix[:,:,i].flatten())
    henon_map_flatten = henon_map.flatten()

    for i in range(3):
        resultant_matrix_per_channel = []
        for j in range(henon_map_flatten.size):
            resultant_matrix_per_channel.append(image_matrix_bgr[i][j] ^ henon_map_flatten[j])
        resultant_matrix.append(resultant_matrix_per_channel)
    
    resultant_matrix = np.asarray(resultant_matrix)
    # print(resultant_matrix.shape)
    resultant_matrix_b = np.reshape(resultant_matrix[0], [w,h])
    resultant_matrix_g = np.reshape(resultant_matrix[1], [w,h])
    resultant_matrix_r = np.reshape(resultant_matrix[2], [w,h])
    resultant_matrix = np.dstack((resultant_matrix_b, resultant_matrix_g, resultant_matrix_r))
    print(resultant_matrix)
    # im = Image.fromarray(resultant_matrix, 'RGB')
    # im = Image.new("RGB", (w, h, d))
    # pix = im.load()
    # for x in range(w):
    #     for y in range(h):
    #         for z in range(d):
    #             pix[x, y, z] = resultant_matrix[x,y,z]
    path = os.path.join('..', 'Source Code', 'images', 'decrypted')
    newFilePath = path+"\\"+image_name.split('.')[0]+".jpg"
    # im.save(newFilePath, "JPEG")
    # absPath = os.path.abspath(newFilePath)
    # plt.imsave("tes.jpg", resultant_matrix)
    # plt.show()
    # image_to_write = cv2.cvtColor(resultant_matrix, cv2.COLOR_RGB2BGR)
    cv2.imwrite(newFilePath, resultant_matrix)