#!/usr/bin/env python
# coding: utf-8

# ## Hello there! The goal of this Time Series project would be to analyze Tesla's stock trend using Alpha Vantage, comparing the Simple Moving Averages with the actual Closing Prices. "Alpha Vantage Inc. is a leading provider of free APIs for realtime and historical data on stocks and cryptocurrencies."

# ## I will aim to demonstrate both the code and the stock market aspect, in a way that a non-technical or inexperienced audience will understand! 

# In[1]:


# Make the necessary imports immediately. This is good convention and will reduce any future headaches.
# Pandas to collect our data in a dataframe
# Alpha Vantage module to actually collect/manipulate the data
# Matplotlib/Plotly/Chart Studio's new libraries for Data Visualization!

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
import chart_studio
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px


# In[2]:


# Here we are simply connecting to Chart Studio (Plotly's new online service).
# The online services are completely FREE. Simply input your username and API key.
chart_studio.tools.set_credentials_file(username='aladin.feratovic', api_key='vWYy7MFd2cIQUkNVqOtd')


# In[3]:


# Necessary code to allow our Chart Studio visualizations to be publically available online.
chart_studio.tools.set_config_file(world_readable=True,
                                 sharing='public')


# In[4]:


# Similar to what we did earlier; this is our API key for Alpha Vantage's stock market API. Also FREE.
api_key = 'X29H06HO2X1S1RC9'


# ## Here we are basically pulling the Daily Stock prices of Tesla and instantiating variables to be converted to Pandas dataframes. We do so by 'plugging' in our API keys and choosing Pandas as the format for the required parameters.

# In[5]:


timesrs = TimeSeries(key=api_key, output_format='pandas')
data_timesrs, meta_data_timesrs = timesrs.get_daily(symbol='TSLA', outputsize='full')

techInd = TechIndicators(key=api_key, output_format='pandas')
data_techInd, meta_data_techInd = techInd.get_sma(symbol='TSLA', interval='daily', time_period=10, 
                                                  series_type='close')


# In[6]:


data_timesrs.head(4)


# In[7]:


# This code is used to change the name of our Closing price column from '4. close to Closing Price'
# Remember to set the inplace parameter to True! Otherwise it will not take effect.
data_timesrs.rename(columns={'4. close':'Closing Price'},inplace=True)


# ## In the following code we are converting our prior datasets into Pandas dataframes which will make the Visualizations much easier. We also match their indexes and their shapes, making the number of observations (rows) equal among both dataframes. Otherwise, we'd encounter an error if trying to plot them a graph.

# In[8]:


df1 = data_techInd.iloc[1::]
data_timesrs = data_timesrs.iloc[10:]
df2 = data_timesrs['Closing Price']
df1.index = df2.index

print (df1.shape[0], df2.shape[0])


# In[9]:


data_techInd.head(2)


# In[10]:


# We are now combining both of our dataframes using the Concatenation method! 
total_df = pd.concat([df1, df2], axis=1)
print(total_df.head(10))


# ### As you probably noticed, our index (row of column names) is not lining up properly. We can fix that problem with an easy Data Cleaning technique which is to Reset the Index!

# In[11]:


total_df.reset_index(inplace=True)
total_df.head(10)


# ## Finally, time for some Data Visualization!! The first of our graphs will be created using the Matplotlib library. This is a simple, easy to read static graph comparing Tesla's Closing Price (how their stock moved) versus the Simple Moving Average (how their stock was predicted to move).

# In[12]:


# Create a figure of "subplots". This is an easy method of plotting more than 1 line on our graph.
# Next we add 2 Line plots of data from our total_df dataframe, and a Title to describe the graph.

f, ax = plt.subplots(1, figsize=(20,10))
total_df.plot(kind='line', x='date', y='SMA', color='red', ax=ax)
total_df.plot(kind='line', x='date', y='Closing Price', color='blue', ax=ax)
plt.title('SMA vs. Closing Price for Tesla')
plt.show()


# ## To take our Visualizations even further, we will stay true to Time Series Analysis by creating an interactive graph using Plotly! This will allow us to have more freedom in our graph, to easily compare the Closing Price and the SMA. The graph is Interactive in the sense that you can Zoom in as well as Hover on any line using your mouse, and you will immediately be able to identify Tesla's stock price at that section of time.

# In[13]:


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=total_df['date'], 
        y=total_df['SMA'], 
        name='SMA',
        line=dict(color='firebrick', width=2)))

fig.add_trace(
    go.Line(
        x=total_df['date'],
        y=total_df['Closing Price'],
        name ='Closing Price',
        mode="lines",
        line=go.scatter.Line(color="#99CCFF"),
        showlegend=False))
fig.show()


# ## Now for the Time Series of Stock analysis. Although I am certainly not a professional when it comes to the Stock Marget world, I know a few principles which can used here in practice. For example, whenever the Closing Price is SIGNIFICANTLY lower than the SMA, that would be an ideal time to "Buy-In". In this situation, the stock price is at an unusually high amount of Volatility, and is bound to "correct" itself by increasing closer to the SMA. This also works in Vice-versa; if the Closing Price is SIGNIFICANTLY higher than the SMA, that is the time to sell!
