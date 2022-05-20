#Importing the libraries
!pip install tensorflow==2.2.0
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.preprocessing.image import ImageDataGenerator
tf.__version__

#Preprocessing the Training set
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)
training_set = train_datagen.flow_from_directory('/home/neosoft/Desktop/jupyter/mask_dataset (1)/mask_dataset/train',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')
#Preprocessing the Test set
test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory('/home/neosoft/Desktop/jupyter/mask_dataset (1)/mask_dataset/test',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

#Initialising the CNN
cnn = tf.keras.models.Sequential()

#Step 1 - Convolution
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
#Step 2 - Pooling
cnn.add(tf.ker(pool_size=2, strides=2))as.layers.MaxPool2D
#Adding a second convolutional layer
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
#Step 3 - Flattening
cnn.add(tf.keras.layers.Flatten())
#Step 4 - Full Connection
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
#Step 5 - Output Layer
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

#Compiling the CNN
cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Training the CNN on the Training set and evaluating it on the Test set
cnn.fit(x = training_set, validation_data = test_set, epochs = 25)

import cv2
from matplotlib import pyplot as plt

predict_img = cv2.imread("/home/neosoft/Desktop/jupyter/mask_dataset (1)/mask_dataset/image_2022_04_25T12_57_35_865Z.png")
image = cv2.cvtColor(predict_img, cv2.COLOR_BGR2RGB)
plt.imshow(image)

import numpy as np
from tensorflow.keras.preprocessing import image
#from keras.preprocessing import image
test_image = image.load_img("/home/neosoft/Desktop/jupyter/mask_dataset (1)/mask_dataset/image_2022_04_25T12_57_35_865Z.png", target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
  prediction = 'perfectly wore mask'
else:
  prediction = 'incorrectly wore mask'
print(prediction)  
