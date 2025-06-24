# List of favorite movies
fav_movies = [
    "Vampire Diaries.",
    "Teen Wolf.",
    "The Wolf of Wall Street.",
    "Money Heist.",
    "Prison Break."
]

# Loop through the list using enumerate to get both index and movie
for index, movie in enumerate(fav_movies):
    # Print the index and corresponding movie name
    print(f"Movie {index+1}: {movie}")
