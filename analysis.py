import cv2 
import os
from matplotlib import pyplot as plt 
import cv2 
import numpy as np

def generateHistogram(img, flag):
    fig = plt.figure()
    color = ('b','g','r')
    for i,col in enumerate(color):
        if flag == 'confused':
            img_temp = img[:,:,[i,3]]
            img_temp = img_temp[img_temp[:,:,1] == 255]
            histr = cv2.calcHist([img_temp[:,0]],[0],None,[256],[0,256])
        else:
            histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.title('Histogram Citra '+flag)
        plt.xlim([0,256])
    return fig

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

dir = os.path.join('..', 'Source Code', 'images')
filename = 'ISIC_0024312'

enum = ('original','confused','encrypted')
for i,col in enumerate(enum):
    flag = col
    type = '.png'
    if col == 'original':
        type = '.jpg' 
        flag = ''
    read_dir = os.path.join(dir, flag, filename+type)
    img = cv2.imread(os.path.abspath(read_dir), cv2.IMREAD_UNCHANGED)

    save_dir = os.path.join('..', 'Source Code', 'analyzed')
    
    #Histogram
    generateHistogram(img, col).savefig(os.path.join(save_dir, 'hist_'+col+'_'+filename+'.png'))

    #Correlation
    if col == 'original' or col == 'encrypted':
        save_dir = os.path.join('..', 'Source Code', 'analyzed')
        generateHorizontalCorrelation(img, filename).savefig(os.path.join(save_dir, 'corr_'+col+'_horizontal_'+filename+'.png'))
        generateVerticalCorrelation(img, filename).savefig(os.path.join(save_dir, 'corr_'+col+'_vertical_'+filename+'.png'))
        generateDiagonalCorrelation(img, filename).savefig(os.path.join(save_dir, 'corr_'+col+'_diagonal_'+filename+'.png'))