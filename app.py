import pickle
import streamlit as st
import requests

# OMDb API key
API_KEY = "d7512855"

# fetch movie poster from OMDb
def fetch_poster(movie_title):
    url = "http://www.omdbapi.com/?apikey={}&t={}".format(API_KEY, movie_title)
    
    try:
        data = requests.get(url).json()
        poster = data.get("Poster")

        if poster and poster != "N/A":
            return poster
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"

    except:
        return "https://via.placeholder.com/300x450?text=No+Poster"


# recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:

        movie_title = movies.iloc[i[0]].title

        recommended_movie_names.append(movie_title)
        recommended_movie_posters.append(fetch_poster(movie_title))

    return recommended_movie_names, recommended_movie_posters


# UI
st.header("🎬 Movie Recommender System")

# load model files
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# dropdown movie list
movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# recommendation button
if st.button("Show Recommendation"):

    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])