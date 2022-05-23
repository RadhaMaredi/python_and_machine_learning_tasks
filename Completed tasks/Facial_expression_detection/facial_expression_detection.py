import cv2
#Warnings are provided to warn the developer of situations that aren’t necessarily exceptions
import warnings
from fer import FER

#this function adds an entry into the specifications of the warnings filter.
warnings.filterwarnings('ignore') 

#read the image
image = cv2.imread('/content/img2.jpg')
cv2.imshow(image)

detector = FER()  #fer object
results = detector.detect_emotions(image)  #returns an array of box and expressions probabilities
emotion,score = detector.top_emotion(image)  #returns expression and probability

#draw the bounding box and print the results
x,y,w,h = results[0]['box']         
cv2.rectangle(image, (x,y),(x+w, y+h), (0,187,235),2)
cv2.imshow(image)
print(emotion)
