from itertools import islice
import spacy
nlp = spacy.load('en_core_web_md')

movie_watched = nlp('''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
 Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.''')

# Create a movie class to help distinguish between the movies details
class Movie():

    def __init__(self,movie_name,movie_description,movie_similarity):

        self.movie_name = movie_name
        self.movie_description = movie_description
        self.movie_similarity = movie_similarity

movie_list = []

# Get each movie from the movies.txt file and add it to the movie list in the form of the Movie class
def read_movie_data():

    movie_file = open('movies.txt','r')

    # Split each line into the attributes of the Movie object
    for each_movie in islice(movie_file, 1, None):

        each_movie_element = each_movie.split(":")
        movie_name = each_movie_element[0]
        movie_description = each_movie_element[1]
        movie_similarity = 0

        # Append each line to the movie list
        movie_list.append(Movie(movie_name,movie_description,movie_similarity))

def get_similarities():

    # For each movie get its similarity to the movie watched
    for each_movie in movie_list:

        similarity = nlp(each_movie.movie_description).similarity(movie_watched)
        each_movie.movie_similarity = similarity

def closest_match():

    # Find the closest match by getting the max similarity number from the movie list and print the answer
    closest_movie_match = max(each_movie.movie_similarity for each_movie in movie_list)

    for each_movie in movie_list:

        if each_movie.movie_similarity == closest_movie_match:

            print(f"The next movie that you should watch is : {each_movie.movie_name},{each_movie.movie_description}, it has a similarity rating of : {each_movie.movie_similarity}")

read_movie_data()
get_similarities()
closest_match()