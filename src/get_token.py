import os
import requests
import base64

from dotenv import load_dotenv


def load_spotify_credentials():
    load_dotenv()

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    token = os.getenv("SPOTIFY_CLIENT_TOKEN")

    return client_id, client_secret, token


def save_spotify_token(token):
    env_path = ".env"
    if not os.path.exists(env_path):
        env_path = "../.env"

    with open(env_path, "r") as fr:
        content = fr.read()
        pattern = "SPOTIFY_CLIENT_TOKEN"

        if pattern in content:
            print(f"The pattern '{pattern}' is found in {env_path}")
        else:
            with open(env_path, "a") as fa:
                fa.write(f"\nSPOTIFY_CLIENT_TOKEN={token}")
            print(f"The pattern '{pattern}' has been added to {env_path}")


def get_token():
    client_id, client_secret, token = load_spotify_credentials()

    if token:
        print("Using existing token")
        return token

    client_creds = f"{client_id}:{client_secret}"
    client_creds_encoded = base64.b64encode(client_creds.encode()).decode()

    token_url = "https://accounts.spotify.com/api/token"
    token_headers = {
        "Authorization": f"Basic {client_creds_encoded}"
    }

    token_data = {
        "grant_type": "client_credentials"
    }

    r = requests.post(token_url, headers=token_headers, data=token_data)
    if r.status_code not in range(200, 299):
        print(f"error {r.status_code}. Could not authenticate with Spotify API")
        return None

    token_response_data = r.json()
    access_token = token_response_data.get('access_token')

    save_spotify_token(access_token)

    return access_token


access_token = load_spotify_credentials()[2]

if not access_token:
    access_token = get_token()
