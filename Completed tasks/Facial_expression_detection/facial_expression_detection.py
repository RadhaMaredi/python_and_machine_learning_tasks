!pip install fer

import cv2
from google.colab.patches import cv2_imshow  #in google colab cv2 is not worked that's why we imported it

#Warnings are provided to warn the developer of situations that aren’t necessarily exceptions
import warnings

#this function adds an entry into the specifications of the warnings filter.
warnings.filterwarnings('ignore') 

from fer import FER

#read the image
image = cv2.imread('/content/img2.jpg')
cv2_imshow(image)

detector = FER()  #fer object
results = detector.detect_emotions(image)  #returns an array of box and expressions probabilities
emotion,score = detector.top_emotion(image)  #returns expression and probability

x,y,w,h = results[0]['box']         #draw the bounding box
cv2.rectangle(image, (x,y),(x+w, y+h), (0,187,235),2)

cv2_imshow(image)
print(emotion)
