Loop invariant is max_score = max(max_score, score_of_movie_i), where score_of_movie_i = uniqueness_i * discussability_i

**Initialization**

Initialization will be true as soon as all variables get their initial values, including 
movies, movies_pairs, friends, watched_movies, similar_movies, mean_of_movies, max_score.

**Maintenance**

Every loop iteration max_score is recalculated, max_score = max(max_score, score_i).
The invariant is not broken.

**Termination**

The algorithm terminates as soon as all movies from the movies list have been scored. The movie with the highest score is returned.