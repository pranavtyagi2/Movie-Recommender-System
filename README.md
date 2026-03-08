# 🎬 Movie Recommender System

A **Content-Based Movie Recommender System** built using **Python, Machine Learning, and Streamlit**.
The system recommends similar movies based on a selected movie by analyzing movie metadata and computing similarity between movies.

---

## 🚀 Features

* Recommend **Top 5 similar movies**
* Interactive **Streamlit web interface**
* Displays **movie posters using OMDb API**
* Fast recommendations using **precomputed similarity matrix**

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* OMDb API

---

## ⚙️ How It Works

1. Movie datasets are merged and cleaned.
2. Important features like **genres, keywords, cast, and crew** are combined into a single column called **tags**.
3. Text data is converted into vectors using **CountVectorizer**.
4. **Cosine Similarity** is calculated between movies.
5. When a user selects a movie, the system recommends the **most similar movies**.

---

## 📂 Project Structure

Movie-Recommender-System
│
├── app.py
├── movie_recommender.ipynb
├── requirements.txt
├── README.md
│
└── model
├── movie_list.pkl
└── similarity.pkl

---

## ▶️ Installation

Clone the repository:

git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset** containing movie metadata such as title, genres, cast, crew, and overview.

---

## 🖥️ Demo

Select a movie from the dropdown and the system will recommend **5 similar movies along with their posters**.

---

## 🔮 Future Improvements

* Add **movie ratings and overview**
* Implement **hybrid recommendation system**
* Improve UI with **better styling**
* Deploy the app online

---

## 📌 Author

Developed by **Pranav Tyagi**

---

⭐ If you like this project, consider giving it a **star** on GitHub!
