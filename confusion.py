import numpy as np
import cv2

def generateArnoldMap(image):
    print("Begin confusion...")
    N = image.dimension[0]
    # initial values
    p = image.key.arnold.p
    q = image.key.arnold.q
    iter = image.key.arnold.iter
    
    # create x and y for pixel position
    x,y = np.meshgrid(range(N),range(N))
    # create meshgrid for new position
    xmap = (x+y*p) % N
    ymap = (x*q+y*(p*q+1)) % N
    arnold_map = image.matrix
    for i in range(iter):
        arnold_map[xmap,ymap] = arnold_map[x,y]

    return arnold_map

def reconstructArnoldMap(image):
    print("Begin unconfusion...")
    N = image.dimension[0]
    p = image.key.arnold.p
    q = image.key.arnold.q
    iter = image.key.arnold.iter

    # create x and y for pixel position
    x,y = np.meshgrid(range(N),range(N))
    # create meshgrid for new position
    xmap = (x+y*p) % N
    ymap = (x*q+y*(p*q+1)) % N
    arnold_map = image.matrix
    for i in range(iter):
        arnold_map[x,y] = arnold_map[xmap,ymap]

    return arnold_map