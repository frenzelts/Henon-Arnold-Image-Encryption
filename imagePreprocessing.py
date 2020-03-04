# from PIL import Image
# import matplotlib.pyplot as plt
import numpy as np
import cv2

def getImageMatrix(image):
    image_matrix = cv2.imread(image)
    # image_matrix = cv2.cvtColor(image_matrix, cv2.COLOR_BGR2RGB)
    # print(image_matrix)
    # print("separator")
    # new = np.array(image_matrix)
    # print(image_matrix)
    return image_matrix

def getImageSize(image_matrix):
    image_size = image_matrix.shape
    return image_size