# 🎵 Song-Recommendor 🎧

A Spotify-style song recommendation web app built with **Streamlit** and powered by **content-based filtering**.  
Just search your favorite song and get smart, personalized recommendations in a beautiful UI.

---

## 🚀 Features

- 🔍 **Smart Search**: Enter any song title and get similar tracks recommended.  
- 🖼️ **Album Art Display**: Album covers fetched from the Spotify API.  
- 🌐 **Streamlit Web App**: Instant feedback, styled UI, and responsive design.  
- 📦 **Pickle-Based Data Loading**: Fast loading using precomputed similarity matrices.  

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python (Pandas, Scikit-learn)  
- **ML Approach**: Content-based filtering using cosine similarity  
- **Data**: Preprocessed `.pkl` files for quick startup  

---

## 📁 Directory Structure

├── app.py # Streamlit web app 
├── song_recommendation.ipynb # Notebook for building and testing recommender logic 
├── .gitignore # Excludes large model/data files


> ⚠️ The files `df.pkl`, `similarity.pkl`, and their compressed versions are ignored in git.  
> You need to **generate or download** them manually to run the app.

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Song-Recommendor.git
cd Song-Recommendor
```
### 2. Create & Activate Virtual Environment (optional)
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```
### 4. Add Data Files
#### Ensure the following files are placed in the root directory (they are not version-controlled):
```
df.pkl — DataFrame of songs
similarity.pkl — Similarity matrix (cosine similarity)
```

You can generate them by running the notebook:
jupyter notebook song_recommendation.ipynb

###🚦 Running the App
```bash
streamlit run app.py
```
Open the browser at the URL displayed (usually http://localhost:8501) to interact with the app.

📸 Screenshots
![App Preview](https://i.postimg.cc/c4zKm0Gx/Preview.png)

