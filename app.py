import streamlit as st 
import joblib
from tfr import processing
import pandas as pd
import numpy as np
from newsdataapi import NewsDataApiClient
import requests



pipe = joblib.load('Pipeline_new.plk')

apikey='04b51110e62d2ee68a1d58b2834fc9ed'
url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=in&max=20&apikey={apikey}"
response = requests.get(url)
data = response.json()


response = requests.get(url)

data = pd.DataFrame(response.json()['articles'])

st.dataframe(data)



# for article in data['articles']: 
#     st.success(f"Headline: {article['title']}")
#     st.success(f"Description: {article['description']}\n")

