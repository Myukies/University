import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Picture.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(img)
plt.show()

rows, cols, dim = img.shape

M = np.float32([[1, 0, -150],
                [0, 1, -150],
                [0, 0, 1]])

translated_img = cv2.warpPerspective(img, M, (cols, rows))

plt.axis('off')
plt.imshow(translated_img)
plt.show()
plt.imsave("Picture_translated.jpg", translated_img)