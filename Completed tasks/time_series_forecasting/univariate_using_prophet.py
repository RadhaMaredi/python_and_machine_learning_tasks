#import libraries
import pandas as pd
import fbprophet
import matplotlib.pyplot as plt
%matplotlib inline
from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics
from fbprophet.plot import plot_cross_validation_metric

#read dataset
df=pd.read_csv('monthly-milk-production-pounds.csv')

#drop the nan values
df.drop(168,axis=0,inplace=True)

#change the column names of datetime and target
df.columns=["ds","y"]
df.plot()

#convert to stationary data
df['y']=df['y']-df['y'].shift(1)

#convert to date time
df['ds']=pd.to_datetime(df['ds'])
df['y'].plot()

# intiialize the Model
model=Prophet()
model.fit(df)
model.seasonalities
model.component_modes

# Create future dates of 365 days
future_dates=model.make_future_dataframe(periods=365)

# Prediction
prediction=model.predict(future_dates)
print(prediction[['ds','yhat','yhat_lower','yhat_upper']].tail())
print(prediction[['ds','yhat','yhat_lower','yhat_upper']].head())

# plot the predicted projection
#black-actual  values,daarkblue-predicted, light blue-trend
model.plot(prediction);

# Visualize Each Components[Trends,Weekly]
model.plot_components(prediction);

#cross validation
df_cv=cross_validation(model,horizon="365 days",period='180 days',initial='1095 days')
print(df_cv)

#performance metrix
df_performance=performance_metrics(df_cv)

#visualize the rmse
plot_cross_validation_metric(df_cv,metric='rmse')
