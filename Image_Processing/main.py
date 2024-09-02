import pandas as pd
import numpy as np
from glob import glob
import cv2
import matplotlib.pyplot as plt

# Reading images
dog_files = glob('images/dog*.jpg')
# print(len(dog_files))
img_mpl = plt.imread(dog_files[0])
img_cv2 = cv2.imread(dog_files[0])
img_mpl.shape, img_cv2.shape
img_mpl / 255, img_cv2 / 255
pd.Series(img_mpl.flatten()).plot(kind='hist', bins=50, title='Diagramma')
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img_mpl)
ax.axis('off')
plt.show()

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(img_mpl[:, :, 0], cmap='Reds')
axs[1].imshow(img_mpl[:, :, 1], cmap='Greens')
axs[2].imshow(img_mpl[:, :, 2], cmap='Blues')
axs[0].axis('off')
axs[1].axis('off')
axs[2].axis('off')
axs[0].set_title('Red channels')
axs[1].set_title('Green channels')
axs[2].set_title('Blue channels')
plt.show()


fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img_cv2)
axs[1].imshow(img_mpl)
axs[0].axis('off')
axs[1].axis('off')
axs[0].set_title('CV2 Image')
axs[1].set_title('Matplotlib Image')
plt.show()

# Converting images
img_cv2_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
fix, ax = plt.subplots()
ax.imshow(img_cv2_rgb)
ax.axis('off')
plt.show()
