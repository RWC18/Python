#%pylab inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('gg.jpg')
imgplot = plt.imshow(img)
plt.show()