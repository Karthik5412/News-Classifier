import streamlit as st 
import joblib
from tfr import processing
import pandas as pd
import numpy as np
from newsdataapi import NewsDataApiClient
import requests



pipe = joblib.load('Pipeline_new.plk')
enc = joblib.load('Label_encoder.plk')


apikey='04b51110e62d2ee68a1d58b2834fc9ed'
url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=in&max=20&apikey={apikey}"
response = requests.get(url)

response = requests.get(url)

data = pd.DataFrame(response.json()['articles'])
data = data.rename(columns={'title' : 'headlines'})

data['category'] = enc.inverse_transform(pipe.predict(data[['headlines', 'description', 'content']]))

st.dataframe(data[['headlines', 'description', 'content', 'url', 'image', 'category']])



# for article in data['articles']: 
#     st.success(f"Headline: {article['title']}")
#     st.success(f"Description: {article['description']}\n")

