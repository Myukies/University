import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Picture.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(img)
plt.show()

rows, cols, dim = img.shape

M = np.float32([[1, 0.9, 0],
             	[0.2, 1  , 0],
            	[0, 0  , 1]])

sheared_img = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5)))

plt.axis('off')
plt.imshow(sheared_img)
plt.show()
plt.imsave("Picture_sheared.jpg", sheared_img)