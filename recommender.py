import pandas as pd, joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import clean_text
class Recommender:
    def __init__(self,csv,models):
        self.csv=csv; self.models=models; models.mkdir(exist_ok=True)
        self.df=pd.read_csv(csv)
        self.df['c']=self.df.storyline.apply(clean_text)
        self.v=TfidfVectorizer(stop_words='english')
        self.m=self.v.fit_transform(self.df.c)
    def recommend_from_text(self,t,top_k=5):
        q=self.v.transform([clean_text(t)])
        s=cosine_similarity(q,self.m)[0]
        idx=s.argsort()[::-1][:top_k]
        return self.df.iloc[idx].to_dict('records')
