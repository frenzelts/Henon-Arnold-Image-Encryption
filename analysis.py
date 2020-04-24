import cv2 
import os
import histogram as hist
import correlation as corr

dir = os.path.join('..', 'Source Code', 'images')
filename = 'ISIC_0024306'

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
    hist.generateHistogram(img, col).savefig(os.path.join(save_dir, 'hist_'+col+'_'+filename+'.png'))

    #Correlation
    if col == 'original' or col == 'encrypted':
        save_dir = os.path.join('..', 'Source Code', 'analyzed')
        corr.generateHorizontalCorrelation(img, filename).savefig(os.path.join(save_dir, 'corr_'+col+'_horizontal_'+filename+'.png'))
        corr.generateVerticalCorrelation(img, filename).savefig(os.path.join(save_dir, 'corr_'+col+'_vertical_'+filename+'.png'))
        corr.generateDiagonalCorrelation(img, filename).savefig(os.path.join(save_dir, 'corr_'+col+'_diagonal_'+filename+'.png'))

