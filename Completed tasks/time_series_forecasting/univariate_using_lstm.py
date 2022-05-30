import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
%matplotlib inline
import tensorflow as tf
from tensorflow import keras
#from tensorflow.keras import layers
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Flatten,Dropout

df1 = pd.read_csv("/home/neosoft/Downloads/archive (6)/Google_Stock_Price_Train.csv")

#distribution is not gaussion so used minmaxscaler it returns feature ranges  0 to 1 range
sc=MinMaxScaler(feature_range=(0,1))
df1_scaled_train = sc.fit_transform(df1)

hops = 60 #choose a number of time steps
total_len = df1_scaled_train.shape[0] #define input sequence

#preparing independent and dependent features
x_train=[]
y_train=[]
for i in range(60,total_len):
    #fine end of this pattern
    #gathering input and output parts of the pattern
    x_train.append(df1_scaled_train[i-60:i])
    y_train.append(df1_scaled_train[i])
x_train=np.array(x_train)
y_train=np.array(y_train)

print(x_train)
print(y_train)
print(len(x_train))
print(len(y_train))

#reshape it to (batche_size(#size of inputs),timesteps,input_dimension)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

#build the model
model = Sequential()
#addign layer1 LSTM
#input_shape=(no.of time steps(60),last feature of x_train)
model.add(LSTM(units=100, return_sequences=True,input_shape=(x_train.shape[1],1)))
model.add(Dropout(0.2))
#adding layer2 LSTM
model.add(LSTM(units=100,return_sequences=True))
model.add(Dropout(0.4))
#adding layer3 LSTM
model.add(LSTM(units=100,return_sequences=True))
model.add(Dropout(0.6))
#adding layer4 LSTM
model.add(LSTM(units=100))
model.add(Dropout(0.4))
#adding Dense layer
model.add(Dense(units=1))
model.compile(optimizer="adam",loss='mean_squared_error')
model.summary()

#fitting the RNN  to the traing dataset
epochs = model.fit(x_train,y_train,epochs=100,batch_size=32,validation_split=0.2)

#plot the loss graph
plt.plot(epochs.history['loss'], label='train')
plt.plot(epochs.history['val_loss'], label='test')
plt.title('Loss Graph') 
plt.xlabel('Epochs')  
plt.ylabel('Loss') 
plt.legend();

#prepare test data set and try predicting 2017 values for the same.
df1_test=pd.read_csv('/home/neosoft/Downloads/archive (6)/Google_Stock_Price_Test.csv')
print(df1_test.shape)
print(df1_test['Open'].plot())

df1_total = pd.concat([df1['Open'],df1_test['Open']],axis=0)
#print(df1_total)
df1_new = df1_total.values
#print(len(df1_new))
test_arr = df1_new[len(df1_new)-len(df1_test)-60:]
#verify if 80 reords are present or not. 20 from test data and last 60 records from train dataset
#print(len(test_arr))
print(test_arr)

#convert it into 60 features and 1 out as we did for train data set
#before that scale it
test_arr_1 = sc.transform(test_arr.reshape(-1,1))

n_hops = 60
n_features = 1
x_test = []
#dont require y_test this time as we are going to predict the values
y_test=[]
for i in range(n_hops, test_arr_1.shape[0]):
    x_test.append(test_arr_1[i-n_hops:i])
x_test=np.array(x_test)

#predicting the values
y_test_pred = model.predict(x_test)

#getting original values by doing the inverse transoform
y_test_predict_actual = sc.inverse_transform(y_test_pred)

#compare predicted and actual values by creaing a Dataframe
test_pred_1 = pd.DataFrame(y_test_predict_actual,columns=['Predicted'])
test_actual_1 = df1_test[['Date','Open']]
full_test_actual_1=pd.concat([test_pred_1,test_actual_1],axis=1)
print(full_test_actual_1)

#visualization
full_test_actual_1.index=pd.to_datetime(full_test_actual_1['Date'])
plt.plot(full_test_actual_1["Open"],color='red',label='actual')
plt.plot(full_test_actual_1["Predicted"],color='blue',label='pred')
plt.plot()
plt.legend()
