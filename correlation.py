import numpy as np
import matplotlib.pyplot as plt
import cv2 

def generateHorizontalCorrelation(img, filename):
    x = img[0:img.shape[0]-1,0:img.shape[1]-1,0]
    y = img[1:img.shape[0],0:img.shape[1]-1,0]
    fig = plt.figure()
    plt.scatter(x, y, s=0.01, alpha=0.5)
    plt.title(filename+'\nHorizontal pixel correlation')
    plt.xlabel('pixel value at (x,y)')
    plt.ylabel('pixel value at (x+1,y)')
    return fig

def generateVerticalCorrelation(img, filename):
    x = img[0:img.shape[0]-1,0:img.shape[1]-1,0]
    y = img[0:img.shape[0]-1,1:img.shape[1],0]
    fig = plt.figure()
    plt.scatter(x, y, s=0.01, alpha=0.5)
    plt.title(filename+'\nVertical pixel correlation')
    plt.xlabel('pixel value at (x,y)')
    plt.ylabel('pixel value at (x,y+1)')
    return fig

def generateDiagonalCorrelation(img, filename):
    x = img[0:img.shape[0]-1,0:img.shape[1]-1,0]
    y = img[1:img.shape[0],1:img.shape[1],0]
    fig = plt.figure()
    plt.scatter(x, y, s=0.01, alpha=0.5)
    plt.title(filename+'\nDiagonal pixel correlation')
    plt.xlabel('pixel value at (x,y)')
    plt.ylabel('pixel value at (x+1,y+1)')
    return fig
    