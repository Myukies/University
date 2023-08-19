import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Picture.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(img)
plt.show()

cropped_img = img[200:400, 150:300]

plt.axis('off')
plt.imshow(cropped_img)
plt.show()
plt.imsave("city_cropped.jpg", cropped_img)