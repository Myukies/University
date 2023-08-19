import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Picture.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(img)
plt.show()

rows, cols, dim = img.shape

M = np.float32([[-1, 0, cols],
                [ 0, 1, 0   ],
                [ 0, 0, 1   ]])

reflected_img = cv2.warpPerspective(img,M,(int(cols),int(rows)))

plt.axis('off')
plt.imshow(reflected_img)
plt.show()
plt.imsave("Picture_reflected.jpg", reflected_img)