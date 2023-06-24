import cv2
from keras.models import load_model
from PIL import Image
import numpy as np

from numpy import ndarray

model = load_model('BrainTumor10Epoc.h5')

image = cv2.imread('C:\\Users\\Maaz\\Brain Tumor Detection Project\\New folder\\pred\\pred0.jpg')

img = Image.fromarray(image)

img = img.resize((64, 64))

img = np.array(img)

input_img = np.expand_dims(img, axis=0)

result = model.predict(input_img)
print(result)

