import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv


st.set_page_config(page_title="Anime Recommendation System", layout="wide")
st.title("Anime Recommender System")

load_dotenv()

@st.cache_resource
def load_pipeline():
    return AnimeRecommendationPipeline()

init_pipeline = load_pipeline()

query = st.text_input("Enter your anime preferences eg: light hearted anime with romance and comedy")
if st.button("Get Recommendation"):
    if query:
        with st.spinner("Generating recommendation..."):
            try:
                recommendation = init_pipeline.recommend(query)
                st.success("Recommendation generated successfully!")
                st.markdown("### Recommended Anime:")
                st.write(recommendation)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter your anime preferences.")
