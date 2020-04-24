from matplotlib import pyplot as plt 
import cv2 

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
        plt.xlim([0,256])
    return fig