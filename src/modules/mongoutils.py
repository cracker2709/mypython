from pymongo import MongoClient
from bson.json_util import dumps
from objects.Movie import Movie


def get_mongo_database():
    client = MongoClient(
        "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.t6zeh.mongodb.net")
    # attach to db
    db = client.sample_mflix
    return db


def get_movies_json():
    db = get_mongo_database()
    cursor = db.movies.find({}, {"title": 1, "type": 1, "year": 1, "poster": 1}).limit(10);
    list_movies = list(cursor)
    return dumps(list_movies)


def get_movies_html():
    retval = []
    db = get_mongo_database()
    # With poster only
    # cursor = db.movies.find({},{"title": 1, "plot":1,type": 1, "year": 1, "poster":{"$exists": True}, "_id":0}).limit(10);

    # With or without poster
    pipe = [
        {
            "$project": {
                "title": 1,
                "type": 1,
                "year": 1,
                "plot": 1,
                "poster": {"$ifNull": ["$poster", "static/images/no_image.png"]}}
        },
        {
            "$limit": 10
        }
    ]

    cursor = db.movies.aggregate(pipe)
    list_movies = list(cursor)
    for movie in list_movies:
        print(f'{movie["title"]} - {movie["type"]} - {movie["year"]} - {movie["poster"]}')
        movie_obj = Movie(movie["title"], movie["type"], movie["year"], movie["plot"], movie["poster"])
        retval.append(movie_obj)
    return retval
