import cv2
import numpy as np
import matplotlib.pyplot as plt

#provide the path for testing cofing file and tained model form colab
net = cv2.dnn.readNetFromDarknet("/home/neosoft/Desktop/yolov3_3classes/yolov3_cutom.cfg",r"/home/neosoft/Desktop/yolov3_3classes/yolov3_custom_5000.weights")

# Change here for custom classes for trained model 
class_names = ['mask','no_mask','improper_mask']

# Load names of classes and get random colors
classes = []
with open('/home/neosoft/Desktop/yolo3_dataset/classes.names','r') as f:
    classes = [line.strip() for line in f.readlines()]
print(classes)

#read the image and resize the image
my_img = cv2.imread('/home/neosoft/Desktop/1.jpg')
my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB)
plt.imshow(my_img)

my_img = cv2.imread('/home/neosoft/Desktop/1.jpg')
my_img = cv2.resize(my_img,(1280,720))
my_img.shape      #height,width, no.of channels

ht, wt, _ = my_img.shape

#it returns an 4d array/blob for input img, (img,scalefactor(1/n),size,mean subtraciton,swapRB)
# convert the images list into an OpenCV-compatible blob
blob = cv2.dnn.blobFromImage(my_img, 1/255, (416,416),(0,0,0),swapRB = True, crop = False)  
blob.shape

#blob object is given given as input to the network
net.setInput(blob)

#yOLOv3 has 3 output layers (82, 94 and 106) as the figure shows.

#getLayerNames(): Get the name of all layers of the network.

#getUnconnectedOutLayers(): Get the index of the output layers.
    
 
last_layer = net.getUnconnectedOutLayersNames()
layer_out = net.forward(last_layer)
layer_out
layer_out[0].shape
layer_out[0][0]

boxes =[]
confidences = []
class_ids = []

for output in layer_out:
    for detection in output:
        score = detection[5:]
        class_id = np.argmax(score)
        confidence = score[class_id]
        
        if confidence > 0.6:
            
            center_x = int(detection[0] * wt)
            center_y = int(detection[1] * ht)
            w = int(detection[2] * wt)
            h = int(detection[3]* ht)
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            boxes.append([x,y,w,h])
            confidences.append((float(confidence)))
            class_ids.append(class_id)
            
#Performs non maximum suppression(nms) given boxes and corresponding scores.
indexes = cv2.dnn.NMSBoxes(boxes, confidences,.5,.4)  
indexes

font = cv2.FONT_HERSHEY_PLAIN #font style
colors = np.random.uniform(0,255,size = (len(boxes),3))

m=0
n=0
k=0
if len(indexes) > 0:
    for i in indexes.flatten():
        x,y,w,h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str((int(confidences[i] *100)))
        
        if label == "mask":
            cv2.rectangle(my_img,(x,y),(x+w, y+h), (0,255,0),2)
            cv2.putText(my_img,label + " "+ confidence +'%', (x,y-8), font, 2, (0,255,0),2)
            m=m+1
            
        if label == "no_mask":
            cv2.rectangle(my_img,(x,y),(x+w, y+h), (0,0,255),2)
            cv2.putText(my_img,label + " "+ confidence +'%', (x,y-18), font, 2, (0,0,255),2)
            n=n+1
            
        if label == "improper_mask":
            cv2.rectangle(my_img,(x,y),(x+w, y+h), (255,0,0),2)
            cv2.putText(my_img,label + " "+ confidence +'%', (x,y-18), font, 2, (255,0,0),2)
            k=k+1

print("With mask: " + str(m))
print("without mask: "+str(n))
print("improper mask: "+str(k))
    
cv2.imshow('img',my_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


