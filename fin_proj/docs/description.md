**Description**

The movie recommedation system finds movie with the highest score and returns its title.

**input:** formatted data

**output:** name of recommended movie

**format of input data**

The system expects to get dict in the following format:
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
<span>**pair must consist of two different movies</span><br>


**explanation:**

| Algorithm | Comments |
| --- | --- |
| 1. Processing data|
| 1.1. Converting list of movies that friend watched to set |
| 1.2. Creating dict of format<br>{watched_movie_title: number_of_views} |
| 1.2.1. Creating list of watched movies |
| 1.2.2. Applying Counter function to created list |
| 1.3. Creating dict of format<br>{movie_title: set_of_similar_movies} |
| 1.3.1. Converting edge list to adjacency list |
| 1.3.2. Finding all similar films (dfs) for every movie |
| 1.4. Creating dict of format<br>{movie_title: mean} |
| 1.4.1. Performing sets intersection for every friend<br>(set of similar movies & set of movies that friend watched) |
| 1.4.2. Summarizing length of intersections |
| 2. Calculating recommendation |
| 2.1. Obtaining discussability |
| 2.2. Obtaining uniqueness |
| 2.3. Calculating movie score |
| 2.4. Returning for a movie with the highest score |


