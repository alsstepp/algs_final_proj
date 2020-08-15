from collections import Counter
from collections import defaultdict
from addfuncs import *


class MovieRecommendationSystem:
    def __init__(self, data):
        if any(key not in data for key in ('movies', 'movies_pairs', 'friends')):
            raise Exception("Data has wrong format")

        # list of movies
        self.movies = data['movies']
        # list of movies pairs (edge list)
        self.movies_pairs = data['movies_pairs']
        # dict - k: friend_name, v: list_of_watched_movies
        self.friends = {k: set(v) for k, v in data['friends'].items()}
        # dict - k: watched_movie_title, v: number_of_views
        self.watched_movies = self.__get_watched_movies()
        # dict - k: movie_title, v: set_of_similar_movies
        self.similar_movies = self.__get_similar_movies()
        # dict - k: movie_title, v: mean
        self.mean_of_movies = self.__get_mean_of_movies()

    # returns a dict where k - watched movie title, value - number of views of this movie
    def __get_watched_movies(self):
        # obtaining flatten list of watched movies
        # movies titles are unique
        # if some friend watched a film several times it is expected that the film is mentioned just once in json file
        # For example, Ivan watched "The Matrix" 3 times, but json file contains "Ivan": ["The Matrix", "In Time"]
        watched_movies_lst = [movie for movies in self.friends.values() for movie in movies]
        # counting how many friends watched movie
        watched_movies = Counter(watched_movies_lst)

        return watched_movies

    # returns a dict where k - movie title, v - set of similar movies
    def __get_similar_movies(self):
        if len(self.movies_pairs) == 0:
            return {}

        def _dfs(v, graph, visited, similar_movies):
            visited[v] = True

            for u in graph[v]:
                if not visited[u]:
                    similar_movies.add(u)
                    _dfs(u, graph, visited, similar_movies)

        # dfs algorithms is used to find all movies in the same connected component (similarity)
        def dfs(v, graph):
            visited = {k: False for k in graph.keys()}
            similar_movies = set()
            _dfs(v, graph, visited, similar_movies)

            return similar_movies

        # converts edge list to adjacency list
        def egde2adjacency(edge_list):
            adj_list = defaultdict(set)

            for movie_1, movie_2 in edge_list:
                adj_list[movie_1].add(movie_2)
                adj_list[movie_2].add(movie_1)

            return adj_list

        adj_list = egde2adjacency(self.movies_pairs)
        movies_list = adj_list.keys()
        similar_movies = dict()

        # adding all similar movies to dict
        for movie_title in movies_list:
            similar_movies[movie_title] = dfs(movie_title, adj_list)

        return similar_movies

    # returns a dict where k - movie title, v - mean
    def __get_mean_of_movies(self):
        mean_of_movies = {}
        for movie_title in self.movies:
            if len(self.friends) == 0:
                mean_of_movies[movie_title] = 0
            else:
                mean_of_movies[movie_title] = sum([len(self.similar_movies.get(movie_title, set()) & self.friends[friend]) for friend in self.friends]) / len(self.friends)

        return mean_of_movies

    # returns discussability metric for given movie
    def __calc_discussability(self, movie_title):
        # if movie was not watched there is nothing to discuss
        if movie_title not in self.watched_movies:
            return 0

        return self.watched_movies[movie_title]

    # returns uniqueness metric for given movie
    def __calc_uniqueness(self, movie_title):
        mean = self.mean_of_movies[movie_title]

        # movie is absolutely unique if nobody watched it
        if movie_title not in self.watched_movies.keys() or mean == 0:
            return float('inf')

        return 1 / mean

    # main function that calculates movies score and returns movie with the highest score
    def get_recommendation(self, movie_title=""):
        # if movie title is provided searching will be performed on similar movies
        if movie_title not in self.similar_movies.keys():
            movies_list = self.movies
        else:
            movies_list = self.similar_movies[movie_title]

        rec_movie, max_score = ("", -1)
        for movie in movies_list:
            uniqueness = self.__calc_uniqueness(movie)
            discussability = self.__calc_discussability(movie)

            # if movie was not watched its uniqueness is inf and discussability = 0, 0*inf is indeterminate form
            # in this case such a film will be recommended in order to encourage watching new films
            if uniqueness == float("inf") and discussability == 0:
                rec_movie, max_score = movie, uniqueness
                break

            score = uniqueness * discussability
            if score > max_score:
                rec_movie, max_score = movie, score

        print(f"Recommended movie: {rec_movie}")
        return rec_movie


if __name__ == "__main__":
    data = load_data("data/data.json")

    mrs = MovieRecommendationSystem(data)
    mrs.get_recommendation()
