from PIL import Image
from numpy import random
import numpy as np
import cv2
import pytesseract
from pytesseract import Output
import time

x = random.randint(100)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    k = cv2.waitKey(0) & 0xff
    filename = f'{x}.png'
    if faces.any():
        cv2.imwrite(filename, img)
    val = input(f"Enter {x} if you are a human being: ")
    break
cap.release()

filename = 'receipt.png'
img = np.array(Image.open(filename))
image = cv2.imread(filename)
results = pytesseract.image_to_data(image, output_type=Output.DICT)
P_No_is_next = 0
Items_is_next = 0
for i in range(0, len(results["text"])):
    x = results["left"][i]
    y = results["top"][i]

    w = results["width"][i]
    h = results["height"][i]
    text = results["text"][i]
    conf = int(results["conf"][i])

    if conf > 70:
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    parcel_no_text = []
    if text in ['Parcel', 'Industries', 'Receipt']:
        pass
    elif text == 'P_No:':
        Parcel_no = results["text"][i + 1]
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    elif text == 'Items:':
        No_of_Items = results["text"][i + 1]
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

fname = f'{val}_Parcel_no.png'
cv2.imwrite(fname, img)

print(f'Parcel_no {Parcel_no}')
print(f'No_of_Items {No_of_Items}')





