import pickle
import streamlit as st
import pandas as pd


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
       movie_id = movies.iloc[i[0]].movie_id
       recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

page_bg_img = '''
<style>
      .stApp { 
  background-image: url("https://payload.cargocollective.com/1/11/367710/13568488/MOVIECLASSICSerikweb_2500_800.jpg");
  background-size: cover;
}


.header {
        color: white;
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        margin-bottom: 20px;
    }
    .recommendation {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
        background-color: rgba(255,255,255,0.8);
    }
    .button {
        background-color: #ff5733; 
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 1.2em;
        font-weight: bold;
        border-radius: 5px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #c70039;
    }

    .selectbox-container {
        position: relative;
        background-color: rgba(240, 255, 240, 0.8); /* Semi-transparent background for better readability */
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
        margin: 10px 0; /* Add margin to space it from other elements */
    }
    .selectbox-container select {
        color: black; /* Change the text color inside the selectbox */
        font-size: 1.2em; /* Optional: increase font size */
    }
    .selectbox-label {
        color: white; /* Label text color */
        font-size: 1.2em; /* Optional: increase font size */
        margin-bottom: 6px;
        display: block;
    }
</style>'''



st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown('<h1 class="header">Movie Recommender System</h1>', unsafe_allow_html=True)

movies_dict = pickle.load(open('movie_dict_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
st.markdown('<label class="selectbox-label">Type or select a movie from the dropdown</label>', unsafe_allow_html=True)
st.markdown('<div class="selectbox-container">', unsafe_allow_html=True)
selected_movie = st.selectbox("", movie_list)
st.markdown('</div>', unsafe_allow_html=True)





if st.button('Show Recommendations', key='recommendations', help='Click to get movie recommendations', use_container_width=True):
    with st.spinner('Fetching recommendations...'):
        recommended_movie_names = recommend(selected_movie)
    
    if recommended_movie_names:
        cols = st.columns(len(recommended_movie_names))
        for i, col in enumerate(cols):
            with col:
                with st.container():
                    st.markdown(f'<div class="recommendation"><h3>{recommended_movie_names[i]}</h3></div>', unsafe_allow_html=True)
                    
    else:
        st.warning('No recommendations available.')

