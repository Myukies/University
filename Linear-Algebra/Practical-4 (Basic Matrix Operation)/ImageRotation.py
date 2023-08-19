import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Picture.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(img)
plt.show()

rows, cols, dim = img.shape

angle = np.radians(65)

M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
            	[np.sin(angle), np.cos(angle), 0],
            	[0, 0, 1]])

rotated_img = cv2.warpPerspective(img, M, (int(cols),int(rows)))

plt.axis('off')
plt.imshow(rotated_img)
plt.show()
plt.imsave("Picture_rotated.jpg", rotated_img)