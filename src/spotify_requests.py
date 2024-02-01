import json
import os
import requests

from check_status_code import is_status_good


def search_for(search_object):
    object_name = input(f"Enter name of the {search_object}: ")
    access_token = os.getenv("SPOTIFY_CLIENT_TOKEN")

    query = object_name.replace(' ', '+')

    search_url = "https://api.spotify.com/v1/search"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "q": query,
        "type": search_object,
        "limit": 1
    }

    response = requests.get(search_url, headers=headers, params=params)

    if is_status_good(response.status_code):
        print(json.dumps(response.json(), indent=4))  # If we want to observe the whole json
        return object_name
    else:
        return None

    # if is_good(response.status_code):
    #     # THIS IS FOR DATA GENERATING
    #     with open(f"../jsons/{search_object}.json", "w+") as fw:
    #         fw.write(f"{params['q']}\n\n")
    #         fw.write(json.dumps(response.json(), indent=4))
    #
    #     # track_data = response.json()['tracks']['items'][0]
    #     # print(track_data)
    #     # return track_data
