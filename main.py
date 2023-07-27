import streamlit as st
import langchain_helper as lh

st.title("Anime Recommendation Base on Genre")
genre = st.sidebar.selectbox("Select Genre",("Isekai","Adventure","Pirates","Magic","Comedy"))

if genre:
    response =lh.animeandplot(genre)
    st.header(response["anime_name"])
    description= response["desc"]
    st.write(description)
