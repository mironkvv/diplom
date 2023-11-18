import configuration
import requests
import Data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

def get_track():
    track_body = post_new_order(Data.User_body)
    track_put = str(track_body.json()['track'])
    return track_put

def search_order():
    return requests.get(configuration.URL_SERVICE + configuration.SEARCH_ORDER_PATH + "?t=" + get_track())