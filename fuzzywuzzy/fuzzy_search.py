
from thefuzz import fuzz, process

# calculate similarity of two strings
print(fuzz.ratio("Rattatouille", "rat etoile"))

movie_titles = ["Titanic", "Star Wars", "Star Trek", "Breakfast at Tiffanys"]


# find the most similar match and a quality score
print(process.extractOne("Star Wors", movie_titles))
print(process.extractOne("Star", movie_titles))
print(process.extractOne("Bergfest", movie_titles))
