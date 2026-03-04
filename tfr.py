from sklearn.base import BaseEstimator, TransformerMixin
import re
import string, pandas as pd, numpy as np

class processing_text(BaseEstimator,TransformerMixin) :
    def fit(self, x, y=None ) :
        return self 
    
    def healper(self,x) :
        cleanded = []
        for w in x :
            w = re.sub(r'[^a-zA-z\s]','',w.lower())
            
            w.strip()
            
            cleanded.append(w)
            
        return cleanded
    
    def transform(self, x) :
        x_copy = x.copy()
        for col in x_copy.columns:
            x_copy[col] = self.healper(x_copy[col])
            
        return x_copy
    
class processing_date(BaseEstimator,TransformerMixin) :
    def fit(self, x, y=None ) :
        return self 
    
    def transform(self, x) :
        x['weekday'] = x['date'].dt.weekday
        x['day'] = x['date'].dt.day
        x['month'] = x['date'].dt.month
        x['year'] = x['date'].dt.year
        
        x['day_sine'] = np.sin(2 * np.pi * x['day']- 1/ 31 )
        x['day_cos'] = np.cos(2 * np.pi * x['day']- 1/ 31 )
        
        x['month_sine'] = np.sin(2 * np.pi * x['month']- 1/ 12 )
        x['month_cos'] = np.cos(2 * np.pi * x['month']- 1/ 12 )
        
        x['weekday_sine'] = np.sin(2 * np.pi * x['weekday']- 1/ 7 )
        x['weekday_cos'] = np.cos(2 * np.pi * x['weekday']- 1/ 7 )
        
        return x.drop(columns = ['date', 'day', 'month', 'weekday'])

