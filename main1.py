from fastapi import FastAPI
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

app = FastAPI()

# Spotify Client Credentials
client_id = "9f5d7d77b05645f9a4821fd83904f31d"
client_secret = "ba6a588ba16a4811af0b86f3b6906e49"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = Spotify(client_credentials_manager=client_credentials_manager)

# Playlist IDs
playlists = {
    "happy": "4AjcgKmRSAHvZHHCCiAwcF",
    "sad": "7HODvfDZpJFUCOCz8JT6VK",
    "energetic": "3pm3eHp9nJO5rVAwN27psb"
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Moodify API!"}

@app.get("/playlist/{mood}")
def get_playlist_tracks(mood: str):
    if mood not in playlists:
        return {"error": "Mood not found. Please choose 'happy', 'sad', or 'energetic'."}
    playlist_id = playlists[mood]
    results = sp.playlist_tracks(playlist_id)
    tracks = [
        {"name": track["track"]["name"], "artist": track["track"]["artists"][0]["name"]}
        for track in results["items"]
    ]
    return {"mood": mood, "tracks": tracks}
