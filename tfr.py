from sklearn.base import BaseEstimator, TransformerMixin
import re
import string

class preprocessing(BaseEstimator,TransformerMixin) :
    def fit(self, x, y=None ) :
        return self 
    
    def transform(self,x) :
        cleanded = []
        for w in x :
            w = re.sub(r'[^a-zA-z\s]','',w.lower())
            
            w.strip()
            
            cleanded.append(w)
            
        return cleanded
    
