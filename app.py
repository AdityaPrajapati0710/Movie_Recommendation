# pyright: ignore[reportMissingImports]
import streamlit as st
import pickle
import requests

movie_list = pickle.load(open('movie.pkl', 'rb'))
movie_list = movie_list['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))



st.title("Movie Recommendation App")
Selected_movie_name = st.selectbox(
    "Search for a movie",movie_list
    
)

def fetch_poster(movie_id):
    respons = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data =respons.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    

def recommend(movie):
    movies = pickle.load(open('movie.pkl', 'rb'))
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recomend_movies = []
    recommended_movies_posters = []
    for i in similar_movies:
        movie_id = i[0]
        #Fetch poster from API
        recomend_movies.append(movies.iloc[i[0]].title)
        
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recomend_movies , recommended_movies_posters

if st.button("Recommend !"):
    names,posters =recommend(Selected_movie_name)
    
    
    col1, col2, col3, col4, col5 = st.columns(5)

    fixed_width = 150  # Adjust as needed
    font_size = "15px"  # Customize font size here
    text_color = "#e0e0e0"  # Optional: match your dark theme
    
    padding = "20px"  # Adjust padding as needed

    for i, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            st.image(posters[i], width=fixed_width)
            st.markdown(
                f"<p style='font-size:{font_size}; color:{text_color}; text-align:center;margin-bottom:{padding};'>{names[i]}</p>",
                unsafe_allow_html=True
            )
            
