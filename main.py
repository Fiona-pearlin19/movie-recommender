
from recommender.movie_recommender import MovieRecommender

def main():
    recommender = MovieRecommender("data/movies.csv")

    print("Recommendations for genre='Sci-Fi', language='English':")
    print(recommender.recommend(genre='Sci-Fi', language='English'))

if __name__ == "__main__":
    main()
