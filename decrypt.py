import os
import diffusion as dif
from PIL import ImageTk, Image
import confusion as con
import unconfusion as unc
import resize as res
import cv2
import Image as i

def decrypt(filepath, destination_path):
    im_encrypted = i.Image(filepath, i.Type.ENCRYPTED, cv2.imread(filepath, cv2.IMREAD_UNCHANGED))
    print(im_encrypted.filename)
    
    #begin undiffusion
    im_undiffused = i.Image( "E:\\KULIAH\\Skripsi\\Source Code\\images\\undiffused\\"+im_encrypted.filename.split('.')[0]+".png", i.Type.UNDIFFUSED, dif.pixelManipulation(im_encrypted))
    cv2.imwrite(im_undiffused.filepath, im_undiffused.matrix)

    #begin unconfusion
    im_unconfused = i.Image("E:\\KULIAH\\Skripsi\\Source Code\\images\\unconfused\\"+im_encrypted.filename.split('.')[0]+".png", i.Type.UNCONFUSED, unc.pixelManipulation(im_undiffused))
    cv2.imwrite(im_unconfused.filepath, im_unconfused.matrix)

    #crop border
    im_decrypted = i.Image(destination_path+"\\"+im_encrypted.filename.split('.')[0]+".png", i.Type.DECRYPTED, res.cropBorder(im_unconfused))
    cv2.imwrite(im_decrypted.filepath, im_decrypted.matrix)