import os
from glob import glob
import undiffusion as und
# from PIL import ImageTk, Image


base_skin_dir = os.path.join('..', 'Source Code')
for x in glob(os.path.join(base_skin_dir, 'images', 'transformed', '*.png')):
    filename = os.path.abspath(x)
    resImage = und.pixelManipulation(filename, os.path.basename(x))