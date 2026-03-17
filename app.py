import streamlit as st
from recommender import Recommender
from pathlib import Path
st.title('IMDb Storyline Recommender')
rec = Recommender(Path('data/movies_2024.csv'), Path('models'))
text = st.text_area('Enter storyline')
if st.button('Recommend'):
    for r in rec.recommend_from_text(text):
        st.write(r['title'], '-', r['storyline'])
