#import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from fbprophet import Prophet

df_train = pd.read_csv('/home/neosoft/Downloads/archive (6)/Google_Stock_Price_Train.csv')

#convert into datetime formate and remove volume
df_train['Date'] =pd.to_datetime(df_train['Date'])
df_train['Close']=df_train['Close'].astype(str).str.replace(",","").astype('float64')
df_train = df_train.drop(columns='Volume', axis=1)

#read the test dataset and convert into datetime formate and remove volume
df_test = pd.read_csv('/home/neosoft/Downloads/archive (6)/Google_Stock_Price_Test.csv')
df_test['Date'] =pd.to_datetime(df_test['Date'])
df_test['Close']=df_test['Close'].astype(str).str.replace(",","").astype('float64')
df_test = df_test.drop(columns='Volume', axis=1)

#plot the graph and try to visualize for all columns based on date
plt.figure(figsize=(10,8))
figure, axes = plt.subplots (nrows=2, ncols=2)
axes[0,0].plot(df_train[ 'Date'],df_train[ 'Open'], label='Open') 
axes[0,1].plot(df_train[ 'Date'], df_train['High'], label='High')
axes[1,0].plot(df_train[ 'Date'], df_train['Low'], label='Low') 
axes[1,1].plot(df_train[ 'Date'], df_train[ 'Close'], label='Close')
plt.legend()

#change the column names of datetime and target of train dataset
df_train.rename(columns={'Open':'y', 'Date':'ds'},inplace=True)

#change the column names of datetime and target of test dataset
df_test.rename(columns={'Open':'y', 'Date':'ds'},inplace=True)

#built the lstm model
model = Prophet(interval_width=0.9)
model.add_regressor('High', standardize=False)
model.add_regressor('Low', standardize=False)
model.add_regressor('Close', standardize=False)
model.fit(df_train)

#create a dataframe with required columns
predict = df_test[['ds','High','Low','Close']]

#predict the values
forcast = model.predict(predict)
forcast = forcast[['ds','yhat']]

#concatinate the predicted values and actual values
final_df = pd.concat((forcast['yhat'],df_test),axis=1)

#visualie the values of predicted and actual values
plt.figure(figsize=(8,6))
plt.plot(final_df['ds'],final_df['y'],color='red', label='actual_values')
plt.plot(final_df['ds'],final_df['yhat'],color='blue', label='predicted_values')
plt.legend()

#cross validation
from fbprophet.diagnostics import cross_validation
df_cv=cross_validation(model,horizon="365 days",period='180 days',initial='1095 days')

#perfomance metrix
from fbprophet.diagnostics import performance_metrics
df_performance=performance_metrics(df_cv)

#plot the rmse
from fbprophet.plot import plot_cross_validation_metric
plot_cross_validation_metric(df_cv,metric='rmse')
