import spotipy
import os
import requests
from spotipy.oauth2 import SpotifyOAuth

os.environ["SPOTIPY_CLIENT_ID"] = '6a2960fcefcc48528d58d176502f2f0f'
os.environ["SPOTIPY_CLIENT_SECRET"] = '931c288a3b4143eaa59e860c44337a41'
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost'
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

### 50 is the highest possible limit
results = sp.current_user_saved_tracks(limit=50)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

### need full authorization token - find way for it not to expire
api = requests.get("https://api.spotify.com/v1/playlists/5Kkh15l8ohyMhfGnATt4YV/tracks")
print(api)
#401 error indicates token needs to be refreshed
## need to figure out how to use this https://developer.spotify.com/documentation/general/guides/authorization-guide/
