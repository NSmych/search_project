import os
import requests
import cli

from check_status_code import is_status_good
from data_processing import get_key_data_from


def search_for(search_object):
    object_name = cli.inner_search(search_object)
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
        get_key_data_from(response.json(), search_object)
