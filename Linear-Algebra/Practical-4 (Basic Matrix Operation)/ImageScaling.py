import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Picture.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(img)
plt.show()

rows, cols, dim = img.shape

M = np.float32([[0.5, 0  , 0],
            	[0,   0.8, 0],
            	[0,   0,   1]])

scaled_img = cv2.warpPerspective(img,M,(cols*2,rows*2))

plt.axis('off')
plt.imshow(scaled_img)
plt.show()
plt.imsave("Picture_scaled.jpg", scaled_img)