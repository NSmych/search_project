import os
import requests
import base64
from datetime import datetime, timedelta

from dotenv import load_dotenv


def load_spotify_credentials():
    load_dotenv()

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    token = os.getenv("SPOTIFY_CLIENT_TOKEN")
    current_token_expiration = os.getenv("SPOTIFY_TOKEN_EXPIRY")

    return client_id, client_secret, token, current_token_expiration


def save_spotify_token(token, token_expiration_time):
    env_path = ".env"
    if not os.path.exists(env_path):
        env_path = "../.env"

    with open(env_path, "r") as fr:
        content = fr.read()
        pattern = "SPOTIFY_CLIENT_TOKEN"
        expiry_pattern = "SPOTIFY_TOKEN_EXPIRY"

        if pattern in content:
            print(f"The pattern '{pattern}' is found in {env_path}")
        else:
            with open(env_path, "a") as fa:
                fa.write(f"\nSPOTIFY_CLIENT_TOKEN={token}")
                fa.write(f"\n{expiry_pattern}={token_expiration_time}")
            print(f"The pattern '{pattern}' has been added to {env_path}")


def remove_spotify_token():
    env_path = ".env"
    if not os.path.exists(env_path):
        env_path = "../.env"

    with open(env_path, "r") as fr:
        lines = fr.readlines()

    with open(env_path, "w") as fw:
        for line in lines:
            if not line.startswith("SPOTIFY_CLIENT_TOKEN") and not line.startswith("SPOTIFY_TOKEN_EXPIRY"):
                fw.write(line)


def get_token():
    client_id, client_secret, token, token_expiration_time = load_spotify_credentials()

    if token and token_expiration_time:
        until = datetime.fromisoformat(token_expiration_time)
        current_time = datetime.now()
        if current_time < until:
            print("Using existing token")
            return token
        else:
            remove_spotify_token()

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
    access_token_data = token_response_data.get('access_token')

    until = datetime.now() + timedelta(hours=6)
    token_expiration_time = until.isoformat()

    save_spotify_token(access_token_data, token_expiration_time)

    return access_token_data


access_token, token_expiry = load_spotify_credentials()[2], load_spotify_credentials()[3]

if not access_token or (token_expiry and datetime.now() >= datetime.fromisoformat(token_expiry)):
    access_token = get_token()
