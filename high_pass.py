import numpy as np
import cv2
from matplotlib import pyplot as  plt

img = cv2.imread('a.jpeg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

rows, cols =img.shape
crow, ccol = int(rows/2), int(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs((img_back))

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('input image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap='gray')
plt.title('image after HPF'), plt.xticks([]), plt.yticks()
plt.subplot(133), plt.imshow(img_back)
plt.title('result in jet'), plt.xticks([]), plt.yticks()
plt.show()