import os
from glob import glob
import diffusion as dif
from PIL import ImageTk, Image
import confusion as con
import unconfusion as unc
import resize as res
import cv2

base_skin_dir = os.path.join('..', 'Source Code')
for x in glob(os.path.join(base_skin_dir, 'images', 'encrypted', '*.png')):
    filepath = os.path.abspath(x) #specific path of image
    filename = os.path.basename(x) #image file name
    print(filename)
    
    #Get image matrix and its dimension
    image_matrix = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    image_size = image_matrix.shape
    
    #begin undiffusion
    undiffused_img = dif.pixelManipulation(image_matrix, image_size)
    path = os.path.join('..', 'Source Code', 'images', 'undiffused')
    newFilePath = path+"\\"+filename.split('.')[0]+".png"
    cv2.imwrite(newFilePath, undiffused_img)

    #begin unconfusion
    unconfused_img = unc.pixelManipulation(undiffused_img, undiffused_img.shape)

    #crop border
    image_matrix = res.cropBorder(unconfused_img, unconfused_img.shape)
    path = os.path.join('..', 'Source Code', 'images', 'decrypted')
    newFilePath = path+"\\"+filename.split('.')[0]+".png"
    cv2.imwrite(newFilePath, image_matrix)