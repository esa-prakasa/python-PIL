from PIL import Image
from pylab import *

# open an image
img = Image.open('C:\\Users\\INKOM06\\Pictures\\CERN2019\\cip.TIFF')

imshow(img)
title('RGB Image')
show()
# open an image and then convert to a grayscale
gr_img = Image.open('C:\\Users\\INKOM06\\Pictures\\CERN2019\\cip.TIFF').convert('L')

imshow(gr_img)
title('Grayscale Image')
show()
