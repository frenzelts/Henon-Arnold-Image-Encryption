import os
import diffusion as dif
from PIL import ImageTk, Image
import confusion as con
import resize as res
import cv2
import Image as i

def encrypt(filepath, destination_path, key):
    im_original = i.Image(filepath, i.Type.ORIGINAL, cv2.imread(filepath), key)
    print(im_original.filename)

    #reshape the image into square
    im_reshaped = i.Image("E:\\KULIAH\\Skripsi\\Source Code\\images\\resized\\"+im_original.filename.split('.')[0]+".png", i.Type.RESHAPED, res.resize(im_original), key)
    cv2.imwrite(im_reshaped.filepath, im_reshaped.matrix)
    
    #begin confusion
    im_confused = i.Image("E:\\KULIAH\\Skripsi\\Source Code\\images\\confused\\"+im_original.filename.split('.')[0]+".png", i.Type.CONFUSED, con.pixelManipulation(im_reshaped), key)
    cv2.imwrite(im_confused.filepath, im_confused.matrix)

    # #begin diffusion
    im_diffused = i.Image(destination_path+"\\"+im_original.filename.split('.')[0]+".png", i.Type.ENCRYPTED, dif.pixelManipulation(im_confused), key)
    cv2.imwrite(im_diffused.filepath, im_diffused.matrix)