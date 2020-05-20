import numpy as np
import cv2

def generateArnoldMap(image):
    print("Begin confusion...")
    N = image.dimension[0]
    p = image.key.arnold.p
    q = image.key.arnold.q
    iter = image.key.arnold.iter
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
    print("Begin unconfusion...")
    N = image.dimension[0]
    p = image.key.arnold.p
    q = image.key.arnold.q
    iter = image.key.arnold.iter
    M = np.array(([1,p],[q,p*q+1]))

    arnold_map = np.zeros([N,N,4], np.uint8)
    for i in range(iter):
        for y in range(N):
            for x in range(N):
                pixel_pos = np.array(([x],[y]))
                [x1, y1] = np.mod(np.dot(M,pixel_pos),N)
                arnold_map[x,y] = image.matrix[x1,y1]
    return arnold_map