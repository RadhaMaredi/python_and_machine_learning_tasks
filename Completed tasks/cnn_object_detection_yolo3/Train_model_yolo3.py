#mount with google drive
from google.colab import drive
drive.mount('/content/drive')

#know the files in our folder
!ls '/content/drive/MyDrive/yolo3_custom_data'

#unzip the dataset in to particular directory
!unzip '/content/drive/MyDrive/yolo3_custom_data/custom_data.zip' -d '/content/drive/MyDrive/yolo3_custom_data/'

#clone the the darknet
!git clone 'https://github.com/AlexeyAB/darknet.git' '/content/drive/MyDrive/yolo3_custom_data/darknet'

#change directory to darknet
%cd /content/drive/MyDrive/yolo3_custom_data/darknet

#activate make file
%cd darknet
!sed -i 's/GPU=0/GPU=1/g' Makefile
!sed -i 's/OPENCV=0/OPENCV=1/g' Makefile
!make

#creating training and testing dataset
%cd /content/drive/MyDrive/yolo3_custom_data

#splitting train and test dataset
!python custom_data/creating-files-data-and-name.py
!python custom_data/creating-train-and-test-txt-files.py

#Train the model and download the weights
!darknet/darknet detector train custom_data/labelled_data.data darknet/cfg/yolov3_cutom.cfg custom_weight/darknet53.conv.74 -dont_show
