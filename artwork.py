import requests

def get_artworks(query, limit):
    try:
         response=requests.get("https://api.artic.edu/api/v1/artworks/search",{"q": "Monet"}
       )
         response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete reuest!")
        return
    content=response.json()
    for artwork in content["data"]:
        print(f"*{artwork['title']}")

def main():
    get_artworks("cat", 10)

main()
