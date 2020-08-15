**Description**


The movie recommedation system finds movie with the highest score and returns its title.


**input:** dictionary of the following format  

```
{"movies": [], "movies_pairs": [], "friends": {}}
```

Example of json file in proper format:
```
{
    "movies": [
        "movie_1",
        "movie_2"
    ],

    "movies_pairs": [
        ["movie_1", "movie_2"]
    ],
    
    "friends": {
        "friend_1": ["movie_1", "movie_2"]
    }
}
```
<span>*movies titles must be unique</span><br>
<span>**pair must consist of two different movies</span>


**output**: title of recommended movie


**explanation**

```
# Counter is used by __get_watched_movies()
from collections import Counter
# defaultdict is used by __get_similar_movies()
from collections import defaultdict


class MovieRecommendationSystem:
	# initializing variables with given data
	# python 3 dicts and sets(kind of hash tables) are widely used in this work
	# time complexity of lookup/insert/delete operations of python 3 set is O(1)
	def __init__(self, data):
		# set(hash table) of movies
		#
		# time complexity(list2set) - O(M)
		# space complexity(list2set) - O(M)
        self.movies = set(data['movies'])
        # list of movies pairs (edge list)
        self.movies_pairs = data['movies_pairs']
        # dict - k: friend_name, v: set_of_watched_movies
        #
        # time complexity(list2set) - O(M*F)
		# space complexity(list2set) - O(M*F)
        self.friends = {k: set(v) for k, v in data['friends'].items()}
        # dict - k: watched_movie_title, v: number_of_views
        self.watched_movies = self.__get_watched_movies()
        # dict - k: movie_title, v: set_of_similar_movies
        self.similar_movies = self.__get_similar_movies()
        # dict - k: movie_title, v: mean
        self.mean_of_movies = self.__get_mean_of_movies()
	
	# returns a dict where k - watched movie title and value - number of views of this movie
	#
	# time complexity - O(M)
	# space complexity - O(M)
	def __get_watched_movies(self):
		# for each movie

		# Counter (outside of for loop)
		pass
	
	# returns a dict where k - movie title, v - set of similar movies
	# dfs returns set of similar movies, it is called for each movie
	#
	# time complexity - O(M*(M+P))
	# space complexity - O(M*M)
	def __get_similar_movies(self):
		# dfs algorithms is used to find all movies in the same connected component (similarity)
		#
		# time complexity - O(M+P)
		# space complexity - O(M)
		def dfs(v, graph):
			pass

		# converts edge list to adjacency list
		#
		# time complexity - O(P)
		# space complexity - O(M+P)		
		def egde2adjacency(edge_list):
			# for each edge_pair
			pass
		
		# for each movie call dfs
		pass

	# returns a dict where k - movie title, v - mean
	# similar movies that the user's friends have already seen are found by sets intersection: set_of_similar_movies & set_of_friend_watched_movies
	# sets intersection is performed for every friend and movie
	# 
	# time complexity - O(M*F*min(len(s1),len(s2))
	# space complexity - O(M)
    def __get_mean_of_movies(self):
    	# for each movie
    		# for each friend (mean calculation uses internal loop)
    	pass

	# returns discussability metric for given movie
	# it's a hash table lookup operation
	#
	# time complexity - O(1)
	# space complexity - O(1)	
	def __calc_discussability(self, movie_title):
		pass

	# returns uniqueness metric for given movie
	# it's a hash table lookup operation
	#
	# time complexity - O(1)
	# space complexity - O(1)
	def __calc_uniqueness(self, movie_title):
		pass
	
	# It's the main function that calculates movies score and returns movie with the highest score
	# The function takes one argument - movie_title, which has default value "".
	# If movie_title is provided searching will be performed on silimar movies only(in case if there is such a movie)
	# otherwise it will be performed on all available movies.
	#
	# algorithm:
	# - iterating through movies
	# - calculating score of each movie, score_i = uniqueness_i * discussability_i
	# - storing max score, max_score = max(max_score, score_i)
	# - returning movie title with the highest score
	#
	# time complexity - O(M)
	# space complexity - O(1)
	#
	# overall time complexity - O(M) + O(M*F) + O(M*(M+P)) + O(M*F*min(len(s1),len(s2)) + O(1) -> O(M*F*min(len(s1),len(s2) + M*(M+P))
	# overall space complexity - O(M)+ O(M*F) + O(M**2) + O(1) -> O(M*(M+F))	
	def get_recommendation(self, movie_title=""):
		# for each movie

		pass
```