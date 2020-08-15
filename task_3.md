Time complexity of the algorithm is O(M*F*min(len(s1),len(s2) + M*(M+P)).

Steps that contribute most to time complexity:
	1. finding similar movies for every movie using dfs - O(M*(M+P)). DFS - O(V+E). DFS is called for every movie - O(M*(V+E)), where V=M, E=P
	2. calculating mean values using set intersection aproach - O(M*F*min(len(s1),len(s2)). 
	   Set intersection - O(min(len(s1),len(s2))), for every friend - O(F*min(len(s1),len(s2))), then for every movie - O(M*F*min(len(s1),len(s2)))


```
class MovieRecommendationSystem:
	# time complexity of lookup/insert/delete operations of python 3 set is O(1)
	def __init__(self, data):
		# time complexity(list2set) - O(M)
		self.movies = set(data['movies'])
		self.movies_pairs = data['movies_pairs']
		# time complexity(list2set) - O(M*F)
		self.friends = {k: set(v) for k, v in data['friends'].items()}
		self.watched_movies = self.__get_watched_movies()
		self.similar_movies = self.__get_similar_movies()
		self.mean_of_movies = self.__get_mean_of_movies()
	
	# time complexity - O(M)
	def __get_watched_movies(self):
		# for each movie

		# Counter (outside of for loop)
		pass
	
	# time complexity - O(M*(M+P))
	def __get_similar_movies(self):
		# time complexity - O(M+P)
		def dfs(v, graph):
			pass

		# time complexity - O(P)
		def egde2adjacency(edge_list):
			# for each edge_pair
			pass
		
		# for each movie call dfs
		pass

	# time complexity - O(M*F*min(len(s1),len(s2))
    	def __get_mean_of_movies(self):
    		# for each movie
    			# for each friend
    		pass

	# time complexity - O(1)
	def __calc_discussability(self, movie_title):
		pass

	# time complexity - O(1)
	def __calc_uniqueness(self, movie_title):
		pass
	
	# time complexity - O(M)
	# overall time complexity - O(M) + O(M*F) + O(M*(M+P)) + O(M*F*min(len(s1),len(s2)) + O(1) -> O(M*F*min(len(s1),len(s2) + M*(M+P))
	def get_recommendation(self, movie_title=""):
		# for each movie

		pass
```
