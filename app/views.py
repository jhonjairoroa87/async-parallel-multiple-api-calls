from flask_jsonpify import jsonify

from app import flask_app
from api_clients.api_one import ApiOne
from utils.async_external_data_loader import AsyncExternalDataLoader

import time

@flask_app.route("/")
def index():
    """
    Index view to verify the app is running
    """

    return "is working :)"


@flask_app.route("/sync")
def synchronous():
    """
    Sync view that emulates the sequential call of three api endpoints
    """
    start_time = time.time()

    api_one_instance = ApiOne()

    print("--- %s seconds ---" % (time.time() - start_time))

    users = api_one_instance.get_users()
    posts = api_one_instance.get_posts()
    photos = api_one_instance.get_photos()


    return "I just called users, posts and photos in --- %s seconds ---" % (time.time() - start_time)


@flask_app.route("/async")
def asynchronous():
    """
    Sync view that emulates the async call of three api endpoints
    """

    start_time = time.time()

    api_one_instance = ApiOne()

    data_loader_dict = {
        "users": lambda: api_one_instance.get_users(),
        "posts": lambda: api_one_instance.get_posts(),
        "photos": lambda: api_one_instance.get_photos()
    }

    data_loader_obj = AsyncExternalDataLoader(data_loader_dict)
    final_responses = data_loader_obj.async_load_data()

    users = final_responses['users']
    posts = final_responses['posts']
    photos = final_responses['photos']

    return "I just called users, posts and photos in --- %s seconds ---" % (time.time() - start_time)
