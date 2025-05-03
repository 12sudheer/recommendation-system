# 🎬 Movie Recommendation System

A content-based movie recommender built with **Python**, **Pandas**, **Flask**, and **Cosine Similarity**, deployed locally. Given a movie title, it suggests similar movies using item-based collaborative filtering.

## 📁 Project Structure

```
recommendation-system/
│
├── app/
│   ├── app.py              # Flask application
│   ├── templates/
│   │   └── index.html      # (Optional UI - if added)
│
├── data/
│   ├── movies.csv          # Movie metadata
│   └── ratings.csv         # User ratings
│
├── model/
│   └── similarity.pkl      # Cosine similarity matrix (optional saved model)
│
├── requirements.txt        # All dependencies
└── README.md               # Project documentation
```

##  Getting Started

### 1. Clone the repo:
```bash
git clone https://github.com/12sudheer/recommendation-system.git
cd recommendation-system
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app:
```bash
cd app
python app.py
```

Flask will start at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

##  Example Usage

Use your browser or Postman to call the API:

```bash
http://127.0.0.1:5000/recommend?movie=Toy Story (1995)&n=5
```

### Response:
```json
{
  "recommendations": [
    "A Bug's Life (1998)",
    "Monsters, Inc. (2001)",
    "Finding Nemo (2003)",
    ...
  ]
}
```

## 📊 Dataset Used

- [MovieLens 100K Dataset](https://grouplens.org/datasets/movielens/)
- Contains:
  - `movies.csv` — movieId, title
  - `ratings.csv` — userId, movieId, rating

## 🛠️ Tech Stack

- Python
- Pandas & Scikit-learn
- Flask
- Cosine Similarity

## ✅ Features

- Recommend similar movies based on user ratings
- Simple API endpoint
- Easy to extend with a UI or deep learning model

## 📌 To-Do

- [ ] Add a search UI
- [ ] Deploy on Render/Heroku
- [ ] Add genre filtering
- [ ] Improve recommendation quality using hybrid models
