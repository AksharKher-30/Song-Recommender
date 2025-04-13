import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify credentials
CLIENT_ID = "ced9808185e54d45b76732bd6ccf2c17"
CLIENT_SECRET = "7b13f7e16f1748e2b693739ec6e3f1a6"

# Spotify setup
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load pickled data
music = pickle.load(open('df.pkl', 'rb'))
similar = pickle.load(open('similarity.pkl', 'rb'))

# Function to fetch album art
def get_song_album_cover_url(song_name, artist_name):
    query = f"track:{song_name} artist:{artist_name}"
    result = sp.search(q=query, type='track', limit=1)
    if result and result['tracks']['items']:
        return result['tracks']['items'][0]['album']['images'][0]['url']
    return "https://i.postimg.cc/0QNxYz4V/social.png"

# Recommendation logic
def recommendor(song_name):
    song_index = music[music['song'] == song_name].index[0]
    distances = sorted(list(enumerate(similar[song_index])), reverse=True, key=lambda x: x[1])
    recommended = []
    posters = []
    for i in distances[1:6]:
        song = music.iloc[i[0]].song
        artist = music.iloc[i[0]].artist
        full_title = f"{song} by {artist}"
        recommended.append(full_title)
        posters.append(get_song_album_cover_url(song, artist))
    return recommended, posters

# ----- Custom Styling -----
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(145deg, #1e1e2f, #3a3b5a);
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .block-container {
            padding: 2rem 3rem 5rem;
        }
        .sidebar .sidebar-content {
            background-color: #2c2c3e;
            border-radius: 15px;
            padding: 2rem 1rem;
        }
        .stSelectbox label {
            font-size: 1.1rem !important;
            color: #c0c0c0;
        }
        .stButton>button {
            background-color: #5f5fff;
            color: white;
            border-radius: 10px;
            padding: 0.5rem 1rem;
            transition: all 0.2s ease-in-out;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #6f6fff;
        }
        .recommend-title {
            font-size: 1.3rem;
            font-weight: bold;
            text-align: center;
            margin-top: 0.5rem;
            color: #f0f0f0;
        }
        .recommend-img img {
            border-radius: 20px;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.5);
        }
        .header-title {
            font-size: 2.3rem;
            font-weight: 700;
            text-align: center;
            color: white;
            margin-bottom: 0.5rem;
        }
        .sub-header {
            font-size: 1.4rem;
            text-align: center;
            color: #d6d6d6;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ----- Sidebar Input Panel -----
with st.sidebar:
    st.markdown("## 🎧 Select a Song")
    selected_song = st.selectbox("Choose from the list", music['song'].values)
    clicked = st.button("🔍 Show Recommendation")

# ----- Main Display -----
st.markdown(f"<div class='header-title'>🎵 Music Recommender</div>", unsafe_allow_html=True)

if clicked:
    recommended_names, recommended_posters = recommendor(selected_song)
    st.markdown(f"<div class='sub-header'>Recommendations for <i>{selected_song}</i></div>", unsafe_allow_html=True)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"<div class='recommend-img'><img src='{recommended_posters[i]}' width='100%'></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='recommend-title'>{recommended_names[i]}</div>", unsafe_allow_html=True)
