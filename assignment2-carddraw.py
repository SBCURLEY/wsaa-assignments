# Topic 2: Assignment 2 - CSO API
# Author: Sharon Curley


import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1&jokers_enabled=true"  # including jokers in the deck for fun :)
response = requests.get(url)
#print(response.json())          # print the response for debugging if required, it will print the deck_id.

data = response.json()
deck_id = data["deck_id"]

with open ("deckofcards.json", "w") as fp:
    json.dump(data, fp)

url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(url)
#print(response.json())      # print the response for debugging if required, it will print the cards drawn.

cards = response.json()["cards"]

for card in cards:
    print(f"{card["value"]} of {card["suit"]}")     # Print each card's value and suit