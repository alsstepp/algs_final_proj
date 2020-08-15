import pytest
from copy import deepcopy
from main import MovieRecommendationSystem


data = {
    "movies": [
        "The Matrix",
        "Inception",
        "In Time",
        "Blade Runner",
        "Gladiator",
        "Troy",
        "Seven Samurai",
        "Schindler's List",
        "The Pianist"
    ],

    "movies_pairs": [
        ["The Matrix", "Inception"],
        ["Inception", "In Time"],
        ["The Matrix", "Blade Runner"],
        ["Seven Samurai", "Gladiator"],
        ["Troy", "Gladiator"],
        ["Schindler's List", "The Pianist"]
    ],

    "friends": {
        "Ivan": ["The Matrix", "Inception", "Gladiator", "Troy", "The Pianist"],
        "Maria": ["The Matrix", "In Time", "Inception", "Troy"],
        "Vladimir": ["In Time"],
        "Elena": ["Schindler's List"],
        "Maxim": [],
        "Irina": ["The Matrix", "Blade Runner", "Gladiator"]
    }
}


# @pytest.mark.skip(reason="")
def test_t1():   # unique is returned, unique movie is paired (there is similar movie)
    mrs = MovieRecommendationSystem(data)

    assert mrs.get_recommendation() == "Seven Samurai"


def test_t2():   # unique is returned, unique movie is not paired
    mdata = deepcopy(data)
    mdata["friends"]["Maxim"] = ["Seven Samurai"]
    mdata["movies"].append("New Movie")

    mrs = MovieRecommendationSystem(mdata)

    assert mrs.get_recommendation() == "New Movie"


def test_t3():   # unique is returned if it's in similar list
    mrs = MovieRecommendationSystem(data)

    assert mrs.get_recommendation("Troy") == "Seven Samurai"


def test_t4():   # movie with highest score is returned
    mdata = deepcopy(data)
    mdata["friends"]["Maxim"] = ["Seven Samurai"]

    mrs = MovieRecommendationSystem(mdata)

    assert mrs.get_recommendation() in ("Schindler's List", "The Pianist")


def test_t5():   # similar movie with highest score is returned
    mrs = MovieRecommendationSystem(data)

    assert mrs.get_recommendation("Seven Samurai") in ("Gladiator", "Troy")


def test_t6():   # similar movie with highest score is returned
    mrs = MovieRecommendationSystem(data)

    assert mrs.get_recommendation("Schindler's List") == "The Pianist"


def test_t7():   # similar movie with highest score is returned
    mrs = MovieRecommendationSystem(data)

    assert mrs.get_recommendation("The Matrix") in ("Inception", "In Time")


def test_t8():   # similar movie with highest score is returned
    mrs = MovieRecommendationSystem(data)

    assert mrs.get_recommendation("Blade Runner") == "The Matrix"


def test_t9():   # similar movie with highest score is returned
    mrs = MovieRecommendationSystem(data)

    assert mrs.get_recommendation("Inception") == "The Matrix"


def test_t10():   # similar movie with highest score is returned
    mrs = MovieRecommendationSystem(data)

    assert mrs.get_recommendation("In Time") == "The Matrix"


def test_t11():   # checking boundary conditions
    mdata = {
        "movies": [
            "The Matrix"
        ],

        "movies_pairs": [
        ],

        "friends": {
            "Ivan": ["The Matrix"]
        }
    }

    mrs = MovieRecommendationSystem(mdata)

    assert mrs.get_recommendation() == "The Matrix"


def test_t12():   # checking boundary conditions
    mdata = {
        "movies": [
            "The Matrix"
        ],

        "movies_pairs": [
        ],

        "friends": {
            "Ivan": []
        }
    }

    mrs = MovieRecommendationSystem(mdata)

    assert mrs.get_recommendation() == "The Matrix"


def test_t13():   # checking boundary conditions
    mdata = {
        "movies": [
            "The Matrix"
        ],

        "movies_pairs": [
        ],

        "friends": {
        }
    }

    mrs = MovieRecommendationSystem(mdata)

    assert mrs.get_recommendation() == "The Matrix"


def test_t14():   # checking boundary conditions
    mdata = {
        "movies": [
        ],

        "movies_pairs": [
        ],

        "friends": {
        }
    }

    mrs = MovieRecommendationSystem(mdata)

    assert mrs.get_recommendation() == ""


def test_t15():   # checking boundary conditions
    mdata = {
        "movies_pairs": [
        ],

        "friends": {
        }
    }

    with pytest.raises(Exception):
        mrs = MovieRecommendationSystem(mdata)
