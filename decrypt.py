import os
from glob import glob
import diffusion as dif
from PIL import ImageTk, Image
import confusion as con
import resize as res
import cv2

base_skin_dir = os.path.join('..', 'Source Code')
for x in glob(os.path.join(base_skin_dir, 'images', 'diffused', '*.png')):
    filepath = os.path.abspath(x) #specific path of image
    filename = os.path.basename(x) #image file name
    print(filename)
    
    #Get image matrix and its dimension
    image_matrix = cv2.imread(filepath)
    image_size = image_matrix.shape

    #reshape the image into square
    image_matrix = res.resize(image_matrix, image_size)
    image_size = image_matrix.shape
    
    #begin unconfusion

    #begin undiffusion
    undiffused_img = dif.pixelManipulation(image_matrix, image_size)

    #Save the output
    path = os.path.join('..', 'Source Code', 'images', 'decrypted')
    newFilePath = path+"\\"+filename.split('.')[0]+".png"
    cv2.imwrite(newFilePath, undiffused_img)