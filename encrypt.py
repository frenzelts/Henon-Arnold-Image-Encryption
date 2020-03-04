import os
from glob import glob
import diffusion as dif
from PIL import ImageTk, Image


base_skin_dir = os.path.join('..', 'Source Code')
for x in glob(os.path.join(base_skin_dir, 'images', '*.jpg')):
    filename = os.path.abspath(x)
    resImage = dif.pixelManipulation(filename, os.path.basename(x))