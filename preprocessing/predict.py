import cv2
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras
import queue
import threading

from sinhala_letters import sinhala_letters
from tensorflow.keras.models import Sequential



sys.stdout.reconfigure(encoding='utf-8')
# -*- coding: utf-8 -*-

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, BatchNormalization, Activation, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(16, (3, 3), padding='same', input_shape=(80, 80, 1)),
    BatchNormalization(),
    Activation('relu'),
    Conv2D(16, (3, 3), padding='same'),
    BatchNormalization(),
    Activation('relu'),
    MaxPooling2D((2, 2), padding='same'),
    Conv2D(32, (3, 3), padding='same'),
    BatchNormalization(),
    Activation('relu'),
    Conv2D(32, (3, 3), padding='same'),
    BatchNormalization(),
    Activation('relu'),
    MaxPooling2D((2, 2), padding='same'),
    Conv2D(64, (3, 3), padding='same'),
    BatchNormalization(),
    Activation('relu'),
    Conv2D(64, (3, 3), padding='same'),
    BatchNormalization(),
    Activation('relu'),
    MaxPooling2D((2, 2), padding='same'),
    Flatten(),
    Dense(1024),
    BatchNormalization(),
    Activation('relu'),
    Dense(512),
    BatchNormalization(),
    Activation('relu'),
    Dense(454, activation='linear')  # Adjust activation based on your final task
])
# with open("model/model.json", "r") as json_file:
#     model_json = json_file.read()
#     # print(">>>>>>>>>>>>>>>>>>", model_json)
# # model = keras.models.model_from_json(model_json)
# model = keras.models.model_from_json(model_json, custom_objects={"Sequential": Sequential})
# print(">>>>>>>>>>>>>>>>>> 1")
model.load_weights("model/model_weights.h5")
print(">>>>>>>>>>>>>>>>>> ")

def binarize_image(img):
      mean_val = np.mean(img)
      if mean_val < 128:
        th, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
      else:
        th, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
      # cv2.imwrite(f'images/binarized.jpg', img)
      return img

def segment_characters(binarized_image, original):
    contours, _ = cv2.findContours(binarized_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda contour: cv2.boundingRect(contour)[0])
    character_images = []
    minimum_area_threshold = 0.01 * binarized_image.shape[0] * binarized_image.shape[1]
    for i,contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        if (area > minimum_area_threshold):
          char_image = original[y:y+h, x:x+w]
          character_images.append(char_image)

    return character_images

fileDest = sys.argv[1]
image = cv2.imread(fileDest)
image = image.astype(np.uint8)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binarized = binarize_image(image)
chars = segment_characters(binarized, image)

resized_chars = []
for i, img in enumerate(chars):
    resized_image = cv2.resize(img, (80,80))
    resized_char = cv2.copyMakeBorder(resized_image, 40, 40, 40, 40, cv2.BORDER_CONSTANT, None, value = 0)
    resized_char = cv2.resize(resized_char, (80,80))
    # cv2.imwrite(f'images/{i}final.jpg', resized_char)
    resized_chars.append(resized_char)

normal = []
for img in resized_chars:
  norm = cv2.normalize(img, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
  norm = norm.reshape(80, 80, 1)
  normal.append(norm)

normal_array = np.array(normal)

predictions = model.predict(normal_array)
word = ""

for pred in predictions:
    predicted_class = np.argmax(pred)
    letter = sinhala_letters[predicted_class]
    word += " " + letter

print(word)