from sklearn.base import BaseEstimator, TransformerMixin
import re
import string

class processing(BaseEstimator,TransformerMixin) :
    def fit(self, x, y=None ) :
        return self

    def healper(self, x):
        x = re.sub(r'[^a-zA-z\s]','',x.lower())
        return ' '.join(x.split())

    def transform(self, x) :
        combined = (x['headlines'].astype(str) + ' ' +
                    x['description'].astype(str) + ' ' +
                    x['content'].astype(str))

        return combined.apply(self.healper).tolist()