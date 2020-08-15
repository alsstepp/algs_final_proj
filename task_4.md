Space complexity of the algorithm is O(M*(M+F)).

Steps that contribute most to space complexity:
	<br>1. finding and storing in dict similar movies for every movie using dfs - O(M* M). DFS - O(M). DFS is called for every movie - O(M* M) - the worst case, if graph is fully connected.
	<br>2. converting dict {k: list} to dict {k: set} - O(M* F). Conversion list->set - O(M), for every friend O(M* F) - the worst case when all friends watched all movies 


```
class MovieRecommendationSystem:
	def __init__(self, data):
		# space complexity(list2set) - O(M)
		self.movies = set(data['movies'])
		self.movies_pairs = data['movies_pairs']
		# space complexity(list2set) - O(M*F)
		self.friends = {k: set(v) for k, v in data['friends'].items()}
		self.watched_movies = self.__get_watched_movies()
		self.similar_movies = self.__get_similar_movies()
		self.mean_of_movies = self.__get_mean_of_movies()
	
	# space complexity - O(M)
	def __get_watched_movies(self):
		# for each movie

		# Counter (outside of for loop)
		pass

	# space complexity - O(M*M)
	def __get_similar_movies(self):
		# space complexity - O(M)
		def dfs(v, graph):
			pass

		# space complexity - O(M+P)		
		def egde2adjacency(edge_list):
			# for each edge_pair
			pass
		
		# for each movie call dfs
		pass

	# space complexity - O(M)
    	def __get_mean_of_movies(self):
		# for each movie
			# for each friend
		pass

	# space complexity - O(1)	
	def __calc_discussability(self, movie_title):
		pass

	# space complexity - O(1)
	def __calc_uniqueness(self, movie_title):
		pass

	# space complexity - O(1)
	# overall space complexity - O(M)+ O(M*F) + O(M**2) + O(1) -> O(M*(M+F))	
	def get_recommendation(self, movie_title=""):
		# for each movie

		pass
```
