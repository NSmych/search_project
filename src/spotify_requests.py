import json
import os

import requests


def search_tracks():
    track_name = input("Enter the track name: ")
    access_token = os.getenv("SPOTIFY_CLIENT_TOKEN")

    query = track_name.replace(' ', '+')

    search_url = "https://api.spotify.com/v1/search"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "q": query,
        "type": "track",
        "limit": 10
    }

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code == 200:
        # track_data = response.json()['tracks']['items'][0]
        # print(response.json())
        print(json.dumps(response.json(), indent=4))
        # return track_data
        return track_name
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None


def search_albums():
    print("Searching for albums...")


def search_artists():
    print("Searching for artists...")


def search_genres():
    print("Searching for genres...")
