#import libraries
import pandas as pd
import fbprophet
import matplotlib.pyplot as plt
%matplotlib inline

#read dataset
df=pd.read_csv('monthly-milk-production-pounds.csv')
df.head()
df.tail()

#drop the nan values
df.drop(168,axis=0,inplace=True)
df.tail()

#change the column names of datetime and target
df.columns=["ds","y"]
df.plot()

#convert to stationary data
df['y']=df['y']-df['y'].shift(1)
df.head()

#convert to date time
df['ds']=pd.to_datetime(df['ds'])
df.head()
df['y'].plot()

#import model
from fbprophet import Prophet
dir(Prophet)
df.head()

# intiialize the Model
model=Prophet()
model.fit(df)
model
model.seasonalities
model.component_modes

# Create future dates of 365 days
future_dates=model.make_future_dataframe(periods=365)
df.tail()
future_dates

# Prediction
prediction=model.predict(future_dates)
prediction.head()
prediction[['ds','yhat','yhat_lower','yhat_upper']].tail()
prediction[['ds','yhat','yhat_lower','yhat_upper']].head()

# plot the predicted projection
#black-actual  values,daarkblue-predicted, light blue-trend
model.plot(prediction);

# Visualize Each Components[Trends,Weekly]
model.plot_components(prediction);

#cross validation
from fbprophet.diagnostics import cross_validation
df_cv=cross_validation(model,horizon="365 days",period='180 days',initial='1095 days')
df.head()
df_cv.head()

#performance metrix
from fbprophet.diagnostics import performance_metrics
df_performance=performance_metrics(df_cv)
df_performance.head()

#visualize the rmse
from fbprophet.plot import plot_cross_validation_metric
fig=plot_cross_validation_metric(df_cv,metric='rmse')
