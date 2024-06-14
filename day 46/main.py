from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""
URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which day would you like to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{URL}{date}")
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# ---------------------------------------------------------------------------------------------------------

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Luigi Schmitt", 
        )
    )

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
