from flask import Flask, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

# Set correct paths
BASE_PATH = r"C:\Users\sudheer kumar\PycharmProjects5\CSV.file\recommendation-system"
ratings_path = os.path.join(BASE_PATH, 'data', 'u.data')
movies_path = os.path.join(BASE_PATH, 'data', 'u.item')

# Load ratings
df = pd.read_csv(ratings_path, sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])

# Load movies and assign column names manually
movie_columns = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
                 'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime',
                 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
                 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

movies = pd.read_csv(movies_path, sep='|', encoding='latin-1', header=None, names=movie_columns)

# Merge on movie_id and title
df = pd.merge(df, movies[['movie_id', 'title']], on='movie_id')

# Create user-item matrix
user_movie_matrix = df.pivot_table(index='user_id', columns='title', values='rating').fillna(0)

# Compute cosine similarity
item_similarity = cosine_similarity(user_movie_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# Recommendation endpoint
@app.route('/recommend', methods=['GET'])
def recommend():
    movie = request.args.get('movie')
    n = int(request.args.get('n', 5))

    if movie not in item_similarity_df.columns:
        return jsonify({'error': 'Movie not found'}), 404

    scores = item_similarity_df[movie].sort_values(ascending=False)[1:n+1]
    return jsonify(scores.to_dict())

if __name__ == '__main__':
    app.run(debug=True)

print("Available movies:")
print(list(item_similarity_df.columns)[:50])  # show first 50 titles
