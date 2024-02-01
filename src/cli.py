import requests
import os

welcome = True


def cli():
    global welcome
    if welcome:
        print("Welcome to the Spotify Data Analyzer!")
    print("What would you like to search for?")
    print("1: Tracks\n2: Albums\n3: Artists\n4: Genres")

    options = {"1": search_tracks, "2": search_albums, "3": search_artists, "4": search_genres}
    choice = input("Enter the number of your choice: ")
    try:
        if choice.isnumeric() and 0 < int(choice) <= len(options):
            options[choice]()
        else:
            raise ValueError("Invalid choice")
    except ValueError as e:
        print(e)
        welcome = not welcome
        cli()


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
        # Successful API call
        track_data = response.json()['tracks']['items'][0]
        print(track_data)
        return track_data
    else:
        # API call failed
        print(f"Failed to fetch data: {response.status_code}")
        return None


def search_albums():
    print("Searching for albums...")


def search_artists():
    print("Searching for artists...")


def search_genres():
    print("Searching for genres...")
