import os
import requests
import base64

from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", default="")


def get_token():
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
        print("Could not authenticate with Spotify API")
        return None

    token_response_data = r.json()
    access_token = token_response_data.get('access_token')

    if access_token:
        with open(".env", "r") as fr:
            content = fr.read()
            pattern = "SPOTIFY_CLIENT_TOKEN"

            if pattern in content:
                print(f"The pattern '{pattern}' is found in your .env file")
            else:
                with open(".env", "a") as fa:
                    fa.write(f"\nSPOTIFY_CLIENT_TOKEN={access_token}")
                print(f"The pattern '{pattern}' has been added to your .env file")

    return access_token
