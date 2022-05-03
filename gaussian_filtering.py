import cv2
from matplotlib import pyplot as  plt

img_path = "a.jpeg"
img = cv2.imread(img_path)

blur_img = cv2.GaussianBlur(img, (9,9),sigmaX=34, sigmaY=36)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('input image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur_img)
plt.title('image after GF'), plt.xticks([]), plt.yticks()
plt.show()