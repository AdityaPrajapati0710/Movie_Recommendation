#🎬 Movies Recommendation System

This project implements a content-based movies recommendation system using the TMDB Movie Metadata dataset from Kaggle
. The system recommends similar movies based on their features such as genres, keywords, cast, and crew.

📂 Dataset

Source: TMDB Movie Metadata Dataset

The dataset contains information about:

Movie titles

Genres

Cast and crew

Keywords

Popularity, vote counts, and ratings

⚙️ Features

Data preprocessing and cleaning of movie metadata.

Feature extraction using Bag of Words (BoW) / TF-IDF Vectorization.

Cosine similarity to measure closeness between movies.

Input: Movie title → Output: Top recommended movies.

Implemented in a Jupyter Notebook for easy understanding.

🛠️ Tech Stack

Python 3

Libraries:

pandas, numpy → Data handling

scikit-learn → Vectorization & similarity

nltk → Text preprocessing

matplotlib / seaborn → Visualization







Run all cells and test the system by entering a movie name.

📊 Example

Input:

recommend("The Dark Knight")


Output:

1. Batman Begins  
2. The Dark Knight Rises  
3. Man of Steel  
4. Justice League  
5. Batman v Superman: Dawn of Justice  



