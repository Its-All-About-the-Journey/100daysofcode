import os

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials


URL_TEMPLATE = "https://www.billboard.com/charts/hot-100/{year}-{month}-{day}"


def sp_auth():
    # Environmental variables
    client_id = os.environ.get("CID")
    client_secret = os.environ.get("CS")

    if not client_secret or not client_secret:
        print("No credentials found, exiting.")
        exit()

    try:
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://localhost:9090",
                client_id=client_id,
                client_secret=client_secret,
                show_dialog=True,
                cache_path="../../../token.txt" # Moving outside repo
            )
        )
    
    except:
        print("Spotify authentication failed, exiting.")
        exit()
    
    return sp


def sp_uris(content):
    soup = BeautifulSoup(content, "html.parser")
    songs = soup.find_all("li", class_="chart-list__element")

    sp_uris = list()

    for song in songs:
        rank = song.find("span", class_="chart-element__rank__number").text
        title = song.find("span", class_="chart-element__information__song").text
        artist = song.find("span", class_="chart-element__information__artist").text

        result = sp.search(q=f"track: {title} artist: {artist}", type="track")
        
        try:
            sp_uris.append(result["tracks"]["items"][0]["uri"])

        except:
            print(f"Could not locate: {title} by {artist} ranked {rank}")
    
    return sp_uris


if __name__ == "__main__":
    # Spotify
    sp = sp_auth()

    print("Buidling a new play list based on year month day")
    year, month, day = input("Enter: yyyy mm dd: ").split()

    # Scrape website - Billboards top 100 for specific date
    content = requests.get(URL_TEMPLATE.format(year=year, month=month, day=day))
    
    if not content.ok:
        print("Sorry, was not able to get a billboards top 100 list, exiting.")
        exit()
    
    sp_uris = sp_uris(content.text)

    # If empty list
    if not sp_uris:
        print(f"Sorry, was not able to get a spotify top 100 list, exiting.")
        exit()
    
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user=user_id, name=f"{year}-{month}-{day} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=sp_uris)
