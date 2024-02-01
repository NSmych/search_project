import json
import os
import requests

from check_status_code import is_good


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
        "limit": 10
    }

    response = requests.get(search_url, headers=headers, params=params)

    if is_good(response.status_code):
        # track_data = response.json()['tracks']['items'][0]
        # print(response.json())
        print(json.dumps(response.json(), indent=4))
        # return track_data
        return object_name
    else:
        return None
