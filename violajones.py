import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read image from your local file system
original_image = cv.imread('pexels-vika-glitter-392079-1648387.jpg')

# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
# Load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')
detected_faces = face_cascade.detectMultiScale(grayscale_image,
                                               scaleFactor=1.1,      # Try values between 1.05 and 1.3
                                                minNeighbors=5,       # Increase for fewer false positives
                                                minSize=(30, 30))
for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (100, 100, 56),
        10
    )
# Resize image to fit window (e.g., width=800, height=600)
resized_image = cv.resize(original_image, (800, 800))
cv.imshow('Image', resized_image)
cv.waitKey(0)
cv.destroyAllWindows()
