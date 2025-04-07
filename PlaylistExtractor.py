import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Requirements: pip install -r requirements.txt

# Set credentials
os.environ['SPOTIPY_CLIENT_ID'] = 'a003052323a548bb922ef3fdeaf81b6f'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'b2403dfa0ee346d6bed993cb1c5df864'

# Initialize Spotify API client
client_credentials_manager = SpotifyClientCredentials()
sp = Spotify(client_credentials_manager=client_credentials_manager)

# Playlist URL
playlist_url = "INSERT URL HERE"

# Get playlist ID from URL
playlist_id = playlist_url.split("/")[-1].split("?")[0]

# Fetch playlist metadata
playlist = sp.playlist(playlist_id)
print(f"📀 Playlist Name: {playlist['name']}")
print("🎵 Extracting tracks...\n")

# Extract all tracks with pagination
tracks = []
offset = 0
while True:
    response = sp.playlist_items(playlist_id, offset=offset, limit=100)
    items = response['items']
    if not items:
        break

    for item in items:
        track = item.get('track')
        if track is None:
            continue

        name = track['name']
        artists = ", ".join(artist['name'] for artist in track['artists'])
        tracks.append(f"{len(tracks)+1}. {name} - {artists}")

    offset += len(items)

# Print to console
for entry in tracks:
    print(entry)

# Optional: Save to a file
with open("playlist_tracks.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(tracks))

print("\n✅ Done! Tracks saved to 'playlist_tracks.txt'")