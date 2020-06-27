import numpy as np
import cv2

def generateArnoldMap(image):
    print("Begin confusion...")
    N = image.dimension[0]
    # initial values p, q, and iteration
    # p and q values will always be changed every iteration
    p_all = image.key.arnold.p
    q_all = image.key.arnold.q
    iter = image.key.arnold.iter
    
    # create x and y for pixel position
    x,y = np.meshgrid(range(N),range(N))
    arnold_map = image.matrix
    for i in range(iter):
        # get p and q for each iteration
        p = int(p_all[i%len(p_all)]+p_all[(i+1)%len(p_all)])
        q = int(q_all[i%len(q_all)]+q_all[(i+1)%len(q_all)])
        # create meshgrid for new position
        xmap = (x+y*p) % N
        ymap = (x*q+y*(p*q+1)) % N
        arnold_map[xmap,ymap] = arnold_map[x,y]

    return arnold_map

def reconstructArnoldMap(image):
    print("Begin unconfusion...")
    N = image.dimension[0]
    # initial values p, q, and iteration
    # p and q values will always be changed every iteration
    p_all = image.key.arnold.p
    q_all = image.key.arnold.q
    iter = image.key.arnold.iter

    # create x and y for pixel position
    x,y = np.meshgrid(range(N),range(N))
    arnold_map = image.matrix
    for i in reversed(range(iter)):
        # get p and q for each iteration
        p = int(p_all[i%len(p_all)]+p_all[(i+1)%len(p_all)])
        q = int(q_all[i%len(q_all)]+q_all[(i+1)%len(q_all)])
        # create meshgrid for new position
        xmap = (x+y*p) % N
        ymap = (x*q+y*(p*q+1)) % N
        arnold_map[x,y] = arnold_map[xmap,ymap]

    return arnold_map